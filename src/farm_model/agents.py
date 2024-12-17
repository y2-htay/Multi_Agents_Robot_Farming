import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import mesa
from mesa import Agent
from collections import deque

BATTERY_SKIP_THRESHOLD = 5   # picker - change threshold

# defining the constants for states
FREE = 1   # picker
BUSY = 0   # picker

############################################################
##### DroneRobot Class
############################################################

class DroneRobot(Agent):
    """Drone in the Farm"""
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = "searching"  # "searching", "waiting", or "returning"
        self.battery = 100
        self.battery_tick = 0
        self.type = "drone_robot"
        # For dynamic arrow
        self.prev_pos = pos
        self.heading = (0,0)
        self.signal_queue = []
        self.picker_id_waiting = None

    def arrow_step(self):
        """update position and heading dynamically for the arrow"""
        p_x, p_y = self.prev_pos
        c_x, c_y = self.pos

        if (p_x < c_x):
            self.heading = (1,0)
        elif (p_x > c_x):
            self.heading = (-1,0)
        elif (p_y < c_y):
            self.heading = (0,1)
        elif (p_y > c_y):
            self.heading = (0,-1)

    @property
    def is_busy(self):
        return self.state == BUSY

    def step(self):
        print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}")

        # Decrease battery over time
        self.battery_tick += 1
        if self.battery_tick >= 50:
            self.battery_tick = 0
            self.battery -= 1

        # Return to base if battery is low
        if self.battery <= 20:
            print(f"Drone {self.unique_id} has low battery and is returning to base.")
            self.return_to_base()
            return

        # If waiting for a picker, don't move
        if self.state == "waiting":
            print(f"Drone {self.unique_id} is waiting for a picker {self.picker_id_waiting} at {self.pos}.")

            # Check if the crop is still here and mature
            if not self.check_for_crop():
                # Crop no longer available, revert to searching
                print(f"Drone {self.unique_id}: Crop no longer available, reverting to searching.")
                self.state = "searching"
                return

            # Check if the assigned picker is still coming
            assigned_picker = None
            for agent in self.model.schedule.agents:
                if agent.unique_id == self.picker_id_waiting:
                    assigned_picker = agent
                    break

            # If we can't find the assigned picker, revert to searching
            if assigned_picker is None:
                print(f"Drone {self.unique_id}: Assigned picker no longer exists, reverting to searching.")
                self.state = "searching"
                return

            # Check the assigned picker's state
            if assigned_picker.state in ["waiting", "returning"]:
                # The picker is no longer moving towards this crop, revert to searching
                print(f"Drone {self.unique_id}: Assigned picker {assigned_picker.unique_id} is not coming, reverting to searching.")
                self.state = "searching"
                return

            # Check if the picker arrived at this position
            if any(isinstance(agent, PickerRobot) and agent.pos == self.pos 
                for agent in self.model.grid.get_cell_list_contents(self.pos)):
                print(f"Picker has arrived at {self.pos}. Drone {self.unique_id} will resume searching.")
                self.state = "searching"
            return

        # If searching and we find a crop, signal picker
        if self.check_for_crop():
            print(f"Drone {self.unique_id} found a crop at {self.pos}. Signaling picker.")
            self.signal_picker()
            print("Drone going to signal picker.")
            self.state = "waiting"
            return

        # Move randomly if no crop is found
        self.move_randomly()
        self.arrow_step()

    def check_for_crop(self):
        """ Check for mature crop at the current position """
        from model import CropAgent
        for agent in self.model.grid.get_cell_list_contents(self.pos):
            if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
                print(f"Drone {self.unique_id} has found a mature crop at {self.pos}")
                return True
        return False

    def signal_picker(self):
        """
        Signal a waiting picker about the crop location.
        Now searches a 6x6 area (±3 cells) around the found crop.
        Ensures the chosen cell contains a PathAgent and no TreeAgent or CropAgent.
        """
        from agents import PickerRobot
        from model import TreeAgent, CropAgent, PathAgent

        # Find waiting pickers
        pickers_to_signal = [
            agent for agent in self.model.schedule.agents
            if isinstance(agent, PickerRobot) and agent.state == "waiting"
        ]

        if not pickers_to_signal:
            print("No pickers available to signal.")
            return

        # Calculate Manhattan distance
        def manhattan_distance(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        # Find nearest picker
        nearest_picker = min(
            pickers_to_signal, key=lambda picker: manhattan_distance(self.pos, picker.pos)
        )

        c_x, c_y = self.pos
        target_pos = None

        # Search within ±3 cells from the crop location
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                nx, ny = c_x + dx, c_y + dy
                if 0 <= nx < self.model.grid.width and 0 <= ny < self.model.grid.height:
                    cell_agents = self.model.grid.get_cell_list_contents((nx, ny))
                    # Cell must have a PathAgent and no TreeAgent or CropAgent
                    if any(isinstance(a, PathAgent) for a in cell_agents) and not any(isinstance(a, TreeAgent) or isinstance(a, CropAgent) for a in cell_agents):
                        target_pos = (nx, ny)
                        break
            if target_pos:
                break

        # If no suitable cell found, fallback to the crop position itself
        if not target_pos:
            target_pos = self.pos

        nearest_picker.target_pos = target_pos
        nearest_picker.state = "moving_to_crop"
        self.picker_id_waiting = nearest_picker.unique_id
        print(f"Drone {self.unique_id} signaled Picker {nearest_picker.unique_id} to move to {target_pos}.")

    def move_randomly(self):
        """
        Move the drone to a random neighboring cell.
        """
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=False, include_center=False, radius=1
        )
        new_position = self.random.choice(possible_steps)
        print(f"DroneRobot {self.unique_id} moving from {self.pos} to {new_position}.")
        self.prev_pos = self.pos
        self.model.grid.move_agent(self, new_position)

    def return_to_base(self):
        """
        Move directly toward the base (0,0).
        """
        base_x, base_y = 0, 0
        base_position = (base_x, base_y)

        if self.pos == base_position:
            print(f"DroneRobot {self.unique_id} has reached the base at {self.pos}.")
            return

        current_x, current_y = self.pos
        dx = base_x - current_x
        dy = base_y - current_y
        move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
        move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
        next_position = (move_x, move_y)

        print(f"DroneRobot {self.unique_id} moving from {self.pos} to {next_position}.")
        self.model.grid.move_agent(self, next_position)


##############################################################################################################

class PickerRobot(Agent):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = "waiting"  # "waiting", "moving_to_crop", "picking", "returning"
        self.storage = 0
        self.capacity = 1000
        self.battery = 100
        self.battery_tick = 0
        self.type = "picker_robot"
        self.target_pos = None  # target position (near crop) signaled by drone

    @property
    def Reach(self) -> list:
        positions = []
        c_x, c_y = self.pos
        for x in range(-3,4):
            for y in range(-3,4):
                if 0 <= c_x + x < self.model.grid.width and 0 <= c_y + y < self.model.grid.height:
                    positions.append((c_x + x, c_y + y))
        return positions

    @property
    def is_busy(self):
        return self.state == BUSY

    def step(self):
        print(f"PickerRobot {self.unique_id} at position {self.pos} with storage {self.storage} and battery {self.battery}")

        # Decrease battery over time
        self.battery_tick += 1
        if self.battery_tick >= 50:
            self.battery_tick = 0
            self.battery -= 1

        # Return to base if battery low or storage full
        if self.battery <= 20 or self.storage >= self.capacity:
            print(f"Picker {self.unique_id} is returning to base (battery or storage issue).")
            self.state = "returning"
            self.return_to_base()
            return

        # If moving to a signaled crop
        if self.state == "moving_to_crop":
            print(f"Picker {self.unique_id} is moving to a crop area at {self.target_pos}.")
            if self.pos == self.target_pos:
                print(f"Picker {self.unique_id} has arrived at {self.target_pos}. Starting to pick.")
                self.state = "picking"
            else:
                self.move_towards(self.target_pos)
            return

        # Picking crops
        if self.state == "picking":
            print(f"Picker {self.unique_id} is picking crops within a 6x6 area.")
            self.pick()  # Now 6x6 area
            if self.storage >= self.capacity:
                print(f"Picker {self.unique_id} is full. Returning to base.")
                self.state = "returning"
            return

        # Default state: waiting at the base
        if self.state == "waiting":
            print(f"Picker {self.unique_id} is waiting at the base.")

    def make_decision(self):
        if self.battery <= 20:
            print(f"PickerRobot {self.unique_id} battery low. Returning to base.")
            self.state = "returning"
            return "return_to_base"

        if self.storage >= self.capacity:
            print(f"PickerRobot {self.unique_id} storage full. Returning to base.")
            self.state = "returning"
            return "return_to_base"

        if self.state == "waiting":
            print(f"PickerRobot {self.unique_id} is waiting at the base.")
            return "wait"

        if self.state == "moving_to_crop":
            if self.pos == self.target_pos:
                print(f"PickerRobot {self.unique_id} reached target at {self.pos}.")
                self.state = "picking"
                return "pick"
            else:
                return "move_toward_target"

        if self.state == "picking":
            return "pick"

        if self.state == "returning":
            return "return_to_base"

        return "wait"

    def receive_signal(self, crop_location):
        print(f"PickerRobot {self.unique_id} received crop location: {crop_location}")
        self.state = "moving_to_crop"
        self.target_pos = crop_location

    def pick(self):
        """
        Pick crops within a 6x6 area (±3 cells in both directions).
        """
        from model import CropAgent

        c_x, c_y = self.pos
        picked = False
        # 6x6 area: range(-3,3) gives 6 steps in each direction: -3,-2,-1,0,1,2
        for dx in range(-3, 4):
            for dy in range(-3, 3):
                nx, ny = c_x + dx, c_y + dy
                # Check bounds
                if 0 <= nx < self.model.grid.width and 0 <= ny < self.model.grid.height:
                    cell_agents = self.model.grid.get_cell_list_contents((nx, ny))
                    for agent in cell_agents:
                        if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
                            print(f"Picker {self.unique_id} picked a crop at {(nx, ny)}. Resetting to seed stage.")
                            agent.reset_crop_stage()
                            self.storage += 1
                            picked = True

        if not picked:
            # No mature crops found within reach
            self.state = "waiting"
            print(f"Picker {self.unique_id} found no crops in range. Returning to waiting state.")

    def return_to_base(self):
        """
        Move toward the base (0,0) via BFS, avoiding trees and crop cells.
        """
        from model import TreeAgent, CropAgent, WaterAgent

        base_x, base_y = 0, 0
        base_position = (base_x, base_y)

        if self.pos == base_position:
            print(f"PickerRobot {self.unique_id} has reached the base at {self.pos}.")
            self.state = "waiting"
            self.storage = 0  # Unload crops when at base
            return

        path = self.find_path(self.pos, base_position, avoid_trees_and_crops=True)
        if path and len(path) > 0:
            next_step = path[0]
            if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0:
                print(f"PickerRobot {self.unique_id} is slowing down near the water.")
                self.slowdown_counter -= 1
                return
            cell_agents = self.model.grid.get_cell_list_contents(next_step)
            if any(isinstance(a, WaterAgent) for a in cell_agents):
                print(f"PickerRobot {self.unique_id} entering water at {next_step}.")
                self.slowdown_counter = 5
            print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_step}.")
            self.model.grid.move_agent(self, next_step)
        else:
            print(f"PickerRobot {self.unique_id} could not find a path to the base from {self.pos}.")

    def wait(self):
        pass

    def move_towards(self, target_pos):
        """
        Move towards the target position using BFS pathfinding to avoid obstacles.
        """
        if self.pos == target_pos:
            return

        path = self.find_path(self.pos, target_pos, avoid_trees_and_crops=True)
        if path and len(path) > 0:
            next_step = path[0]
            print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_step}.")
            self.model.grid.move_agent(self, next_step)
        else:
            print(f"PickerRobot {self.unique_id} could not find a path to {target_pos} from {self.pos} this step.")

    def find_path(self, start_pos, goal_pos, avoid_trees_and_crops=False):
        """
        Use BFS to find a path from start_pos to goal_pos.
        If avoid_trees_and_crops is True, skip cells containing TreeAgent or CropAgent.
        """
        from model import TreeAgent, CropAgent

        if start_pos == goal_pos:
            return []

        queue = deque([(start_pos, [])])
        visited = set([start_pos])

        while queue:
            current_pos, path = queue.popleft()
            if current_pos == goal_pos:
                return path

            neighbors = self.model.grid.get_neighborhood(current_pos, moore=True, include_center=False)
            for step in neighbors:
                if step not in visited:
                    cell_agents = self.model.grid.get_cell_list_contents(step)
                    if avoid_trees_and_crops:
                        if any(isinstance(a, TreeAgent) or isinstance(a, CropAgent) for a in cell_agents):
                            continue
                    visited.add(step)
                    queue.append((step, path + [step]))

        return None
