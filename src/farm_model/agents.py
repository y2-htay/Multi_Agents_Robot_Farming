import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)
import mesa
from mesa import Agent
import heapq
from collections import deque


#from .model import FREE, BUSY
#from model import TreeAgent, CropAgent

BATTERY_SKIP_THRESHOLD = 5   # picker - change thereadshold 

#defining the constants for states
FREE = 1         #picker
BUSY = 0         #picker


###################################################################
         ##"""Drone Class ---   Main One with Make Decision"""  still testing 
###################################################################
# class DroneRobot(Agent):
#     """
#     Drone in the farm.
#     """

#     def __init__(self, unique_id, pos, model):
#         print(f"Initializing the drone robot with {unique_id}, {pos}, {model}")
#         super().__init__(unique_id, model)
#         self.pos = pos
#         self.state = "idle"  # Possible states: "idle", "searching", "returning"
#         self.battery = 100
#         self.battery_tick = 0
#         self.type = "drone_robot"
#         # For dynamic heading (optional visualization)
#         self.prev_pos = pos
#         self.heading = (0, 0)

#     ######################################
#     ### Dynamic Arrowhead Visualization
#     ######################################
#     def arrow_step(self):
#         """
#         Update position and heading dynamically for visualization (optional).
#         """
#         p_x, p_y = self.prev_pos
#         c_x, c_y = self.pos

#         if p_x < c_x:
#             self.heading = (1, 0)
#         elif p_x > c_x:
#             self.heading = (-1, 0)
#         elif p_y < c_y:
#             self.heading = (0, 1)
#         elif p_y > c_y:
#             self.heading = (0, -1)

#         # Debugging
#         print(f"Drone {self.unique_id}: Prev Pos = {self.prev_pos}, Current Pos = {self.pos}, Heading = {self.heading}")

#     @property 
#     def is_busy(self):
#         return self.state == BUSY

#     ######################################
#     ### Step Function
#     ######################################
#     def step(self):
#         """
#         Define the action of drones at each step.
#         """
#         print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}")

#         # Decrease battery level
#         self.battery_tick += 1
#         if self.battery_tick >= 50:  # Adjust threshold as needed  # battery dies at 500 steps 
#             self.battery_tick = 0
#             self.battery -= 1
  
#         print(f"Drone Robot {self.unique_id} is taking a step at position {self.pos}.")    ##debug
#         # Make a decision and execute the action
#         action = self.make_decision()
#         print(f"DroneRobot {self.unique_id} decided to: {action}")
#         getattr(self, action)()      #execuse the chosen action 




#     ######################################
#     ### Make Decision
#     ######################################
#     # def make_decision(self):
#     #     """
#     #     Decide the next action for the drone based on its state and surroundings.
#     #     """
#     #     print(f"DroneRobot {self.unique_id} is making a decision.")
#     #     from model import CropAgent

#     #     # If battery is low, return to base
#     #     if self.battery <= 20:
#     #         print(f"DroneRobot {self.unique_id} battery is low. Returning to base.")
#     #         return "return_to_base"

#     #     # If a crop is found at the current position, pause
#     #     if self.check_for_crop():
#     #         print(f"DroneRobot {self.unique_id} found a crop at {self.pos}. Pausing.")
#     #         return "wait"

#     #     # Default action: move randomly
#     #     print(f"DroneRobot {self.unique_id} is searching for crops.")
#     #     return "move_randomly"
    

#     ###### -------------------self-------------------

#     def make_decision(self):
#         """ Decide next action """
#         print(f"Drone Robot {self.unique_id} is making a decision ")
#         from model import CropAgent


#         # if battery is depleted, return to base 
#         if self.battery <= 20:
#             print(f"Drone battery died.Returning to base")
#             self.state = "returning"
#             return "return_to_base"


#         if self.state == "returning":
#             return "return_to_base"
        

#         # # if free/idle , check for nearby crops
#         # if self.state == FREE:
#         #     crop_nearby = any(
#         #         isinstance(agent,CropAgent)
#         #         for agent in self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 3) 

#         #   )
#         #     print(f"DroneRobot {self.unique_id} Crop Nearby: {crop_nearby}") 
#         #     if crop_nearby:
#         #         return "signal_picker"

        

#         ## check for crops 
#         if self.check_for_crop():
#             print(f"Drone {self.unique_id} is reporting a crop at {self.pos}")
#             ## pause for a moment until  the pickers come 
#             return 
        

#         ## move randomly if no crop is found 
#         self.move_randomly()

#         ## update position and heading dynamically 
#         self.arrow_step
            



#     ######################################
#     ### Check for Crops
#     ######################################
#     def check_for_crop(self):
#         """
#         Check if the current cell contains a CropAgent (e.g., strawberries).
#         """
#         from model import CropAgent  # Avoid circular import

#         for agent in self.model.grid.get_cell_list_contents(self.pos):
#             if isinstance(agent, CropAgent):
#                 print(f"DroneRobot {self.unique_id} found a crop at {self.pos}")
#                 return True
#         return False

#     ######################################
#     ### Move Randomly
#     ######################################
#     def move_randomly(self):
#         """
#         Move the drone to a random neighboring cell.
#         """
#         possible_steps = self.model.grid.get_neighborhood(
#             self.pos, moore=True, include_center=False
#         )
#         new_position = self.random.choice(possible_steps)
#         print(f"DroneRobot {self.unique_id} moving from {self.pos} to {new_position}.")
#         self.prev_pos = self.pos
#         self.model.grid.move_agent(self, new_position)

#     ######################################
#     ### Return to Base
#     ######################################
#     def return_to_base(self):
#         """
#         Move directly toward the base to recharge.
#         """
#         base_x, base_y = 0, 0  # Assuming base is at (0, 0)
#         base_position = (base_x, base_y)

#         # If already at the base, stop
#         if self.pos == base_position:
#             print(f"DroneRobot {self.unique_id} has reached the base at {self.pos}.")
#             return

#         # Move directly toward the base
#         current_x, current_y = self.pos
#         dx = base_x - current_x
#         dy = base_y - current_y

#         # Calculate next step
#         move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
#         move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
#         next_position = (move_x, move_y)

#         print(f"DroneRobot {self.unique_id} moving from {self.pos} to {next_position}.")
#         self.model.grid.move_agent(self, next_position)

    

# ###############################################################################
#  #########   test for new added make_decision function -- without signaling (still testing)
# ###############################################################################

# class DroneRobot(Agent):
#     def __init__(self, unique_id, pos, model):
#         super().__init__(unique_id, model)
#         self.pos = pos
#         self.state = "searching"  # Initial state
#         self.battery = 100
#         self.battery_tick = 0
#         self.type = "drone_robot"
#         self.prev_pos = pos  # For heading updates
#         self.heading = (0, 0)
#         #self.step_count = 0  # Initialize step counter 


#     ####Dynamic Arrowhead (new )
#     def arrow_step(self):
#         """update position and heading dynamically for the arrow"""
#         #from mesa.space import MultiGrid     #ensuring grid handling works correctly


#         p_x, p_y = self.prev_pos
#         c_x, c_y = self.pos
        
#         if (p_x < c_x):
#             self.heading = (1,0)
#         elif (p_x > c_x):
#             self.heading = (-1,0)
#         elif (p_y < c_y):
#             self.heading = (0,1)
#         elif (p_y > c_y):
#             self.heading = (0,-1)
#          # Debugging
#         print(f"Drone {self.unique_id}: Prev Pos = {self.prev_pos}, Current Pos = {self.pos}, Heading = {self.heading}")


#     def step(self):
#         """ Define behavior at each step. """
#         print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}")
#         #print(f"Step {self.step} ....")    # testing step count 

#         # Decrease battery over time
#         self.battery_tick += 1
#         if self.battery_tick >= 5:  # Adjust threshold as needed
#             self.battery_tick = 0
#             self.battery -= 1

#         # Make a decision and execute the action
#         action = self.make_decision()
#         print(f"DroneRobot {self.unique_id} decided to: {action}")
#         if action:
#             getattr(self, action)()  # Execute the chosen action

#     def make_decision(self):
#         """ Decide the next action for the drone. """
#         print(f"DroneRobot {self.unique_id} is making a decision.")

#         # Check battery and return to base if necessary
#         if self.battery <= 90:
#             self.state = "returning"
#             return "return_to_base"

#         # If returning to base, continue doing so
#         if self.state == "returning":
#             return "return_to_base"

#         # Check for a crop in the current cell
#         if self.check_for_crop():
#             self.state = "waiting"
#             return "wait"

#         # Default action: move randomly
#         self.state = "searching"
#         return "move_randomly"

#     def check_for_crop(self):
#         """ Check if the current cell contains a CropAgent. """
#         from model import CropAgent  # Avoid circular import
#         for agent in self.model.grid.get_cell_list_contents(self.pos):
#             if isinstance(agent, CropAgent):
#                 print(f"DroneRobot {self.unique_id} found a crop at {self.pos}")
#                 return True
#         return False

#     def move_randomly(self):
#         """ Move the drone to a random neighboring cell. """
#         possible_steps = self.model.grid.get_neighborhood(
#             self.pos, moore=True, include_center=False
#         )
#         if possible_steps:
#             new_position = self.random.choice(possible_steps)
#             print(f"DroneRobot {self.unique_id} moving from {self.pos} to {new_position}.")
#             self.prev_pos = self.pos
#             self.model.grid.move_agent(self, new_position)
#             self.arrow_step()  # Update heading for visualization

#     def return_to_base(self):
#         """ Move directly toward the base to recharge. """
#         base_x, base_y = 0, 0  # Base location
#         if self.pos == (base_x, base_y):
#             print(f"DroneRobot {self.unique_id} has reached the base at {self.pos} at step {self.model.step_count}. Recharging.")
#             self.battery = 100
#             self.state = "searching"
#             return

#         # Move one step closer to the base
#         current_x, current_y = self.pos
#         dx = base_x - current_x
#         dy = base_y - current_y
#         move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
#         move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
#         next_position = (move_x, move_y)

#         print(f"DroneRobot {self.unique_id} moving from {self.pos} to {next_position} (returning to base).")
#         self.prev_pos = self.pos
#         self.model.grid.move_agent(self, next_position)
#         self.arrow_step()  # Update heading for visualization

#     def wait(self):
#         """ Wait in place for a moment. """
#         print(f"DroneRobot {self.unique_id} is waiting at {self.pos} for pickers.")




############################################################
    ##### Drones Classsss for signal test-working   crop aging working 
#############################################################


class DroneRobot(Agent):
    """Drone in the Farm """
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = "searching"  # "searching" or "returning"
        self.battery = 100
        self.battery_tick = 0
        self.type = "drone_robot"
        #for dynamic arrow 
        self.prev_pos = pos # Track previous position ( # for dynamic heading )
        self.heading = (0,0)        
        self.signal_queue = []  # To store crop locations to signal pickers
        self.picker_id_waiting = None


    ######################################
    ### Arrow Step (Drone)
    ######################################



    # Dynamic Arrowhead (new )
    def arrow_step(self):
        """update position and heading dynamically for the arrow"""
        #from mesa.space import MultiGrid     #ensuring grid handling works correctly


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
         # Debugging
        #print(f"Drone {self.unique_id}: Prev Pos = {self.prev_pos}, Current Pos = {self.pos}, Head



    ######################################
    ### Property - is_busy (Drone)
    ######################################


#     @property 
#     def is_busy(self):
#         return self.state == BUSY




    ######################################
    ### Step Function (Drone)
    ######################################


    # def step(self):
    #     """
    #     Define the behavior of drones at each step.
    #     """
    #     print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}")

    #     # Decrease battery over time
    #     self.battery_tick += 1
    #     if self.battery_tick >= 50:  # Adjust this threshold as needed
    #         self.battery_tick = 0
    #         self.battery -= 1

    #     # Return to base if battery is low
    #     if self.battery <= 20:
    #         print(f"Drone {self.unique_id} has low battery and is returning to base.")
    #         self.return_to_base()
    #         return

    #     # If waiting for a picker to arrive, don't move
    #     if self.state == "waiting":
    #         print(f"Drone {self.unique_id} is waiting for a picker {self.picker_id_waiting} at {self.pos}.")
    #         if not self.check_for_crop():
    #             self.state = 'searching'
    #         # Check if a picker has arrived
    #         if any(isinstance(agent, PickerRobot) and agent.pos == self.pos for agent in self.model.grid.get_cell_list_contents(self.pos)):
    #             print(f"Picker has arrived at {self.pos}. Drone {self.unique_id} will resume searching.")
    #             self.state = "searching"
    #         return

    #     # Look for crops
    #     if self.check_for_crop():
    #         print(f"Drone {self.unique_id} found a crop at {self.pos}. Signaling picker.")
    #         self.signal_picker()
    #         print(f"Drone going to signal picker ")
    #         self.state = "waiting"
    #         return

    #     # Move randomly if no crop is found
    #     self.move_randomly()


    #     #update position and heading dynamically (optional for dynamic arrowhead)
    #     self.arrow_step()
        

    ######################################
    ### Step Function (Drone) - test for reach pick 
    ######################################
    

    def step(self):
        """
        Define the behavior of drones at each step.
        """
        print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}")

        # Decrease battery over time
        self.battery_tick += 1
        if self.battery_tick >= 50:  # Adjust this threshold as needed
            self.battery_tick = 0
            self.battery -= 1

        # Return to base if battery is low
        if self.battery <= 20:
            print(f"Drone {self.unique_id} has low battery and is returning to base.")
            self.return_to_base()
            return

        # If waiting for a picker to arrive, don't move
        if self.state == "waiting":
            print(f"Drone {self.unique_id} is waiting for a picker {self.picker_id_waiting} at {self.pos}.")
            if not self.check_for_crop():
                self.state = 'searching'
            # Check if a picker has arrived
            if any(isinstance(agent, PickerRobot) and agent.pos == self.pos for agent in self.model.grid.get_cell_list_contents(self.pos)):
                print(f"Picker has arrived at {self.pos}. Drone {self.unique_id} will resume searching.")
                self.state = "searching"
            return
        

        self.signaled_crop_pos = None  # Add this in the drone's initialization

        if self.check_for_crop():
            if self.signaled_crop_pos == self.pos:
                print(f"Drone {self.unique_id} has already signaled a picker for crop at {self.pos}.")
            else:
                print(f"Drone {self.unique_id} found a new crop at {self.pos}. Signaling picker.")
                self.signal_picker()
                self.signaled_crop_pos = self.pos
                self.state = "waiting"
                return





# ### drone work flow 
#    check battery 
# if <= 20 , return to base and stop further action 

#  if drone is waiting 
# if waiting for pick --
# check if no crop at pos, then switch to searching 
# if picker arrived, switch to searching 
    
# check for crops at current pos
#     if crop found,  signal picker,  and switch to waiting 


# if none of above , move randomly 
        
        
        
        
    # ## change here to check the mature crop 
    # def check_for_crop(self):
    #     """
    #     Check if the current cell contains a CropAgent (strawberries).
    #     """
    #     from model import CropAgent  # Avoid circular import
    #     for agent in self.model.grid.get_cell_list_contents(self.pos):
    #         if isinstance(agent, CropAgent):
    #             print(f"DroneRobot {self.unique_id} found a crop at {self.pos}")
    #             return True
    #     return False



 ##------ test for crop---------------------------------------------------------


    ######################################
    ### Check for crop ( Drone )
    ######################################


    def check_for_crop(self):
        """ Check for mature crop to signal to the pickers"""
        from model import CropAgent   #avoid circular import 
        for agent in self.model.grid.get_cell_list_contents(self.pos):
            if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
                print(f"Drone {self.unique_id} has found a mature crop at {self.pos}")
                return True
        return False

    ### -----------------------------------------------------------------------
    


    ######################################
    ### Signal Picker (Drone)
    ######################################


    ## updated one with the crop stage check in check_for_crop()
    def signal_picker(self):
        """
        Signal pickers at the base about the crop location.
        """
        print(f"Drone bout to signal pickerssss ")
        from agents import PickerRobot

        # Find pickers in the "waiting" state
        pickers_to_signal = [
            agent for agent in self.model.schedule.agents
            if isinstance(agent, PickerRobot) and agent.state == "waiting"
        ]

        if not pickers_to_signal:
            print(f"No pickers available to signal.")
            return

        # Calculate Manhattan distance between the drone and each picker
        def manhattan_distance(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        # Find the nearest picker using the Manhattan distance
        nearest_picker = min(
            pickers_to_signal, key=lambda picker: manhattan_distance(self.pos, picker.pos)
        )

        # # Assign crop location to the nearest picker
        # nearest_picker.target_pos = self.pos  # change here with the reach, cant overlap on the tree grid
        # nearest_picker.state = "moving_to_crop"   
        # self.picker_id_waiting = nearest_picker.unique_id
        # print(f"Drone {self.unique_id} signaled Picker {nearest_picker.unique_id} to move to {self.pos}.")

        #####################
        ## test for pick from reach, not assigning current positio as their target.pos 
        #####################

        # Find all reachable positions around the crop position (drone's position)
        from model import TreeAgent
        reachable_positions = [
           (x, y) for x in range(self.pos[0] - 1, self.pos[0] + 2)
           for y in range(self.pos[1] - 1, self.pos[1] + 2)
           if 0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height
           and not any(isinstance(agent, TreeAgent) for agent in self.model.grid.get_cell_list_contents((x, y)))
           and (x, y) != self.pos  # Exclude the drone's current position
       ]

        if reachable_positions:
           # Assign the nearest reachable position as the target
           target_position = min(
               reachable_positions, key=lambda pos: manhattan_distance(nearest_picker.pos, pos)
           )
           nearest_picker.target_pos = target_position
           nearest_picker.state = "moving_to_crop"
           self.picker_id_waiting = nearest_picker.unique_id
           print(f"Drone {self.unique_id} signaled Picker {nearest_picker.unique_id} to move to {target_position}.")
        else:
           print(f"Drone {self.unique_id} found no reachable position for Picker {nearest_picker.unique_id}.")     


        #####################################
           ### Move Randomly function (Drones)
        ######################################
    
    def move_randomly(self):
        """
        Move the drone to a random neighboring cell, ignoring all terrain constraint restrictions 
        """
        possible_steps = self.model.grid.get_neighborhood(
            self.pos , moore = False, include_center = False, radius=1
        )
        new_position = self.random.choice (possible_steps)
        print (f"DroneRobot {self.unique_id} moving from {self.pos} to {new_position} .")
        self.prev_pos = self.pos
        self.model.grid.move_agent(self, new_position)



        ######################################
           ### Return to bsae Function (Drones) Working 
        ######################################
        
    def return_to_base(self):
            """
            Move directly toward the base to drop off crops or recharge, without avoiding trees or slowing down in water.
            """
            # Define the base coordinates
            base_x, base_y = 0, 0  # Assuming base is at (0, 0)
            base_position = (base_x, base_y)

            # If the drone is already at the base, stop
            if self.pos == base_position:
                print(f"DroneRobot {self.unique_id} has reached the base at {self.pos}.")
                return

            # Determine the direction to the base
            current_x, current_y = self.pos
            dx = base_x - current_x
            dy = base_y - current_y

            # Calculate the next step toward the base
            move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
            move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
            next_position = (move_x, move_y)

            # Move to the next position
            print(f"DroneRobot {self.unique_id} moving from {self.pos} to {next_position}.")
            self.model.grid.move_agent(self, next_position)


    #### Adding utility function for drones to move toward the target 

    ### utility function to calculate the distance 
    # def calculate_distance(pos1, pos2):
    #     """Calculate Manhattan distance between two points."""
    #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    



    

##############################################################################################################


    # class name (inheriting from name):
# class SuperPicker(PickerRobot):
    
#     def __init__(self, unique_id, pos, model):
#         super().__init__(unique_id, pos, model)



#############################################################################################################
           ### PickerRobot Class Initialisation  ( Basic + Extended)
#############################################################################################################

class PickerRobot(Agent):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = "waiting"  # States: "waiting", "moving", "picking", "returning"
        self.storage = 0
        self.capacity = 1000
        self.battery = 100
        self.battery_tick = 0
#        self.type = "picker_robot"
#        self.target_crop = None  # Crop location to move toward target crop


#############################################################
           ### Reach - Property (picker ) - From Basic
#############################################################


    #reach property checking positions only inside the grid. 
    @property
    def Reach(self) -> list:
        positions = []
        c_x , c_y  =self.pos
        for x in range (-3,4):
            for y in range(-3, 4):
                #check if the reach is accessing the positions outside of the grid , 
                if 0 <= c_x + x < self.model.grid.width and 0<= c_y + y < self.model.grid.height:
                    positions.append((c_x + x , c_y + y ))
        return positions



#############################################################
           ### is_busy - Property (picker ) - From Basic
#############################################################

#     @property 
#     def is_busy(self):
#         return self.state == BUSY




#############################################################
           ### Step function (picker ) - Extended ( with signalling )
#############################################################

    # def step(self):
    #     """
    #     Define the behavior of pickers at each step.
    #     """
    #     print(f"PickerRobot {self.unique_id} at position {self.pos} with storage {self.storage} and battery {self.battery}")

    #     # Decrease battery over time
    #     self.battery_tick += 1
    #     if self.battery_tick >= 50:  # Adjust this threshold as needed
    #         self.battery_tick = 0
    #         self.battery -= 1

    #     # Return to base if battery is low or storage is full
    #     if self.battery <= 20 or self.storage >= self.capacity:
    #         print(f"Picker {self.unique_id} is returning to base (battery or storage issue).")
    #         self.return_to_base()
    #         return

    #     # If moving to a signaled crop
    #     if self.state == "moving_to_crop":    #moving_to_crop - move_towared_target() 
    #         print(f"Picker {self.unique_id} is moving to a crop at {self.target_pos}.")
    #         if self.pos == self.target_pos:
    #             print(f"Picker {self.unique_id} has arrived at {self.target_pos}. Starting to pick.")
    #             self.state = "picking"    #pick()
    #         else:
    #             self.move_towards(self.target_pos)  # Move towards the target crop
    #             return      ############## one picker following the first one 

    #     # Picking crops
    #     if self.state == "picking":     #picking - pick()
    #         print(f"Picker {self.unique_id} is picking crops.")
    #         self.pick()
    #         if self.storage >= self.capacity:  # Return to base if full
    #             print(f"Picker {self.unique_id} is full. Returning to base.")
    #             self.state = "returning"  #returning - return_to_base()
    #         return

    #     # Default state: waiting for a signal at the base
    #     if self.state == "waiting":   # waiting - wait()
    #         print(f"Picker {self.unique_id} is waiting at the base.")


#############################################################
           ### Step function (picker ) - Extended ( with signalling ) - testing for pick from reach 
#############################################################

    def step(self):
     """
     Define the behavior of pickers at each step.
     """
     print(f"PickerRobot {self.unique_id} at position {self.pos} with storage {self.storage} and battery {self.battery}")

     # Decrease battery over time
     self.battery_tick += 1
     if self.battery_tick >= 50:  # Adjust this threshold as needed
         self.battery_tick = 0
         self.battery -= 1

     # Return to base if battery is low or storage is full
     if self.battery <= 20 or self.storage >= self.capacity:
         print(f"Picker {self.unique_id} is returning to base (battery or storage issue).")
         self.return_to_base()
         return

     # If moving to a signaled crop
     if self.state == "moving_to_crop":
         print(f"Picker {self.unique_id} is moving to a crop at {self.target_pos}.")
         # Check if the picker is within reach of the crop
         if self.target_pos and self.pos in self.Reach:
             print(f"Picker {self.unique_id} reached the crop within reach. Starting to pick.")
             self.state = "picking"  # Transition to picking state
         else:
             self.move_towards(self.target_pos)  # Move towards the closest reachable grid
         return

     # Picking crops
     if self.state == "picking":
         print(f"Picker {self.unique_id} is picking crops.")
         self.pick()  # Perform the picking operation
         if self.storage >= self.capacity:  # Return to base if full
             print(f"Picker {self.unique_id} is full. Returning to base.")
             self.state = "returning"
         else:
             self.state = "waiting"  # Transition to waiting state after picking
         return

     # Default state: waiting for a signal at the base
     if self.state == "waiting":
         print(f"Picker {self.unique_id} is waiting at the base.")









#############################################################
           ### step function (picker ) - basic- without signalling 
#############################################################
    
#     def step(self):
#         """ 
#         Define the behaviour of the robot at each step 
#         """
#         print(f"PickerRobot {self.unique_id} is stepping at position {self.pos}.")
#         print("battery for ", self.unique_id, " = ", self.battery)
#         print("Storage for", self.unique_id, "=", self.storage)

        
#         #decrease battery level every few ticks 
#         self.battery_tick += 1
        
#         if self.battery_tick == BATTERY_SKIP_THRESHOLD:
#             self.battery_tick = 0
#             self.battery -= 1
            
        
#         print(f"PickerRobot {self.unique_id} is taking a step at position {self.pos}.") #debug
#         #Decision making 
#         action = self.make_decision()
#         print(f"PickerRobot {self.unique_id} decided to : {action }")     #debug print for the visual movement of pickerrobot 
#         getattr(self,action)()        #execuse the chosen action 



#############################################################
           ### Notes - Workflow  (picker) - Extended
#############################################################


# ## work flow for pickers 
# check battery and storage ,  -> not ok, retur to BaseException

# if moving to signaled crop, 
#     state-> moving to crop
#     if picker reach target position (self.target.pos)
#       state-> switch to picking 
# otherwise ---> move towareds to crop 



# if picking crops ( state-> picking)
#     continute picking until storage is full
#     if storage full , then return to base 


# if waiting at the base, (state -> waiting)
#     stay idle and wait for the signal



#############################################################
           ### Receive Signal (picker) - Extended
#############################################################

    def receive_signal(self, crop_location):
        """
        Receive crop location signal from a drone.
        """
        print(f"PickerRobot {self.unique_id} received crop location: {crop_location}")
        self.state = "moving"      ##moving randomly ??
        self.target_crop = crop_location  # assigned here 



# #############################################################
#            ### Pick (Picker) - Extended - Need to fix - to pick from reach
# #############################################################

#     ##  double check here if the grid has  a mature crop and replace it with seed after picking 
#     def pick(self):
#         """
#         Pick crops at the current position.
#         """
#         from model import CropAgent
#         for agent in self.model.grid.get_cell_list_contents(self.pos):
#             if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
#                print(f"Picker {self.unique_id} picked a crop at {self.pos}. Resetting to seed stage")
#                agent.reset_crop_stage()  # changed here 
#                self.storage += 1      #reset to seed stage
#                self.stage = "waiting"     # return to waiting state after picking
#             else:
#                 self.state = "waiting"  # this is the problem, dont forget this 
            

# # self.state = "waiting"
# #             else:
# #                 self.state = "waiting"



#############################################################
           ### Pick (Picker) - Extended 
#############################################################

    # ##  double check here if the grid has  a mature crop and replace it with seed after picking 
    # def pick(self):
    #     """
    #     Pick crops at the current position.
    #     """
    #     from model import CropAgent
    #     reachable = self.Reach
    #     print("reachable", reachable)
    #     for agent in self.model.grid.get_cell_list_contents(self.pos):
    #         if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
    #            print(f"Picker {self.unique_id} picked a crop at {self.pos}. Resetting to seed stage")
    #            agent.reset_crop_stage()  # changed here 
    #            self.storage += 1      #reset to seed stage
    #            self.stage = "waiting"     # return to waiting state after picking
    #         else:
    #             self.state = "waiting"  # this is the problem, dont forget this 



#############################################################
           ### Pick (Picker) - Extended - Still fixing - to pick from reach - test
#############################################################

    def pick(self):
      """
      Pick the crop if it is within the picker's reach.
      """
      print(f"Picker at the nearest place of crop, ready to pick")
      from model import CropAgent

      # Check all positions in reach for mature crops
      for pos in self.Reach:
          for agent in self.model.grid.get_cell_list_contents(pos):
            if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
                print(f"Picker {self.unique_id} picked a crop at {pos}. Resetting to seed stage.")
                agent.reset_crop_stage()  # Reset the crop to the seed stage
                self.storage += 1
                self.state = "waiting"  # Return to waiting state after picking
                return

      # If no crop is found in reach, continue moving toward the target
      print(f"Picker {self.unique_id} found no crop in reach.")
      self.state = "moving_to_crop"





# #############################################################
#            ### Pick( Picker ) - Basic 
# #############################################################
    
            
#     def pick(self):
#         """ 
#         Pick the strawberry if one is in the current cell
#         """
#         print(f"Hey I am ready to pickkkkkkkkkk the strawberry ")
#         from model import CropAgent     #imported locally 
        
#         reachable = self.Reach
        
#         print("reachable", reachable)
        
#         for each in self.Reach:
#             print("Checking, ", each)
            
#             for agent in self.model.grid.get_cell_list_contents(each):
#                 if isinstance(agent, CropAgent):
#                     print(f"PickerRobot {self.unique_id} found a strawberry at {each}")
#                     self.model.grid.remove_agent(agent)
#                     self.model.schedule.remove(agent)
#                     self.storage += 1
#                     print("successfully picked at: ", each, "  Storage: ", self.storage)
#                     continue
#                 print("Not a crop")



#############################################################
           ### Make Decision (picker) ( Extended ) With Signalling 
#############################################################

    def make_decision(self):
        """
        Decide the next action based on the robot's state and surroundings.
        """
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

        if self.state == "moving":
            if self.pos == self.target_crop:
                print(f"PickerRobot {self.unique_id} reached crop at {self.pos}.")
                self.state = "picking"
                return "pick"
            else:
                return "move_toward_target"

        if self.state == "picking":
            return "pick"

        if self.state == "returning":
            return "return_to_base"

        return "wait"
    



#############################################################
           ### Make Decison (picker) - ( Basic ) - Without signalling 
#############################################################
  
#     def make_decision(self):
#       """
#       Decide the next action based on the robot's state and surroundings.
#       """
#       print(f"PickerRobot {self.unique_id} is making a decision.")
#       from model import CropAgent

#       # If the battery is depleted, return to base
#       if self.battery <= 20:
#           print(f"PickerRobot {self.unique_id} battery died. Returning to base.")
#           self.state = "returning"  # added states
#           return "return_to_base"   # return to base instead of wait 

#       # If storage is full, transition to "returning" state and return to base
#       if self.storage >= 100:
#           print(f"PickerRobot {self.unique_id} storage is full. Returning to base.")
#           self.state = "returning"  ## added states 
#           return "return_to_base"   ## return to base instead of wait 

#       # If in "returning" state, continue heading back to the base, confirming it to go to base 
#       if self.state == "returning":
#           return "return_to_base"

#       # If free, check for nearby crops
#       if self.state == FREE:
#           crop_nearby = any(
#             isinstance(agent, CropAgent)
#             for agent in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=3)
#         )
#           print(f"PickerRobot {self.unique_id} Crop Nearby: {crop_nearby}")
#           if crop_nearby:
#               return "pick"
#           else:
#               return "move_randomly"

#       # Default fallback
#       return "wait"




    # ###work flow 
    # check battery  , low-> return to base 
    # check storage, full -> return to base 
    # if waiting > wait
    # if moving (moving to crop) 
    # > if reach to target,  switch to picking 
    # > otherwise, move to target 
    # if picking crops > continue picking
    # if returning (returning to base ) > decide to return to base 
    # default action>  if none of above, just wait



#############################################################
           ### Move Randomly function (picker) - Only Basic
#############################################################

    def move_randomly(self):    # responbile for moving the robot 
        """ 
        Move the robot to a random neighboring cell, avoiding trees , Reduce speed when moving through water
        """
        from model import TreeAgent, WaterAgent   
        #from model import CropAgent
        # imported locally only before they are called / if imported globally at the top, it is circulr dependency with model.py

        # slowing down for moving through water
        if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0 :
            print(f"PickerRobot {self.unique_id} is slowing down near the water")
            self.slowdown_counter -= 1 
            return   # skip  this step 


        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore = True, include_center=False
        )
        valid_steps = [ step for step in possible_steps if not any(isinstance (a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))] 
        # valid_steps = [ 
        #     step for step in possible_steps
        # #     if self.model.grid.is_cell_empty(step)   #check if the cell is empty 
        # #     and not any(isinstance(a,TreeAgent) for a in self.model.grid.get_cell_list_contents(step))     #avoid trees
        #        ##instead of checking ...... 
        #     if not any(isinstance(a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))
        # ]
        print(f"PickerRobot {self.unique_id} valid steps: {valid_steps}")    # debugging 
        if valid_steps:
            #move to a randomly chosen valid step 
            new_position = self.random.choice(valid_steps)
            print(f"PickerRobot {self.unique_id} moving from {self.pos} to {new_position}.")


            #slowing down moving through river 
            if any(isinstance (a, WaterAgent) for a in self.model.grid.get_cell_list_contents(new_position)):
                print ("Picker Robot {self.unique_id} entering water at {self.position}.")
                self.slowdown_counter = 5     #slow down for 5 steps 
            self.model.grid.move_agent(self, new_position)
            print(f"PickerRobot {self.unique_id} moved to {new_position}")     #debug 



#############################################################
           ### Return To Base (picker) 
#############################################################  


    def return_to_base(self):
       """
       Move toward the base to drop off crops, avoiding trees and slowing down in water.
       Uses BFS to find a valid path to the base.
       """
       from model import TreeAgent, WaterAgent

       # Define the base coordinates
       base_x, base_y = 0, 0  # Assuming base is at (0, 0)   ## need to fix for new base position 
       base_position = (base_x, base_y)

       # If the robot is already at the base, stop
       if self.pos == base_position:
           print(f"PickerRobot {self.unique_id} has reached the base at {self.pos}.")
           return

       # BFS setup to find the shortest path to the base
       queue = deque([(self.pos, [])])  # (current position, path taken)
       visited = set()  # To avoid revisiting nodes
       visited.add(self.pos)

       while queue:
           current_pos, path = queue.popleft()

           # Check the current position for base
           if current_pos == base_position:
               # Follow the first step in the path to move toward the base
               if path:
                   next_step = path[0]

                   # Check for water slowdown
                   if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0:
                       print(f"PickerRobot {self.unique_id} is slowing down near the water.")
                       self.slowdown_counter -= 1
                       return  # Skip this step

                   if any(isinstance(a, WaterAgent) for a in self.model.grid.get_cell_list_contents(next_step)):
                       print(f"PickerRobot {self.unique_id} entering water at {next_step}.")
                       self.slowdown_counter = 5  # Slow down for 5 steps

                   # Move to the next step
                   print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_step}.")
                   self.model.grid.move_agent(self, next_step)
               return

           # Explore neighbors
           possible_steps = self.model.grid.get_neighborhood(current_pos, moore=True, include_center=False)
           for step in possible_steps:
               # Avoid revisiting and avoid trees
               if step not in visited and not any(isinstance(a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step)):
                   visited.add(step)
                   queue.append((step, path + [step]))

       print(f"PickerRobot {self.unique_id} could not find a path to the base from {self.pos}.")



#############################################################
           ### Wait function (picker) - Same - for - Basic and Extended 
#############################################################

    def wait(self):
        """
        wait in place when its not full capacity or nothing to do 
        """
        pass



#############################################################
           ### Move Towards Crop (picker) - Extended 
#############################################################


    # def move_towards(self, target_pos):    # target pos,(called in picker step)
    #     """
    #     Move towards the target position.
    #     """
    #     current_x, current_y = self.pos
    #     target_x, target_y = target_pos

    #     # Calculate the direction
    #     dx = target_x - current_x
    #     dy = target_y - current_y
    #     move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
    #     move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
    #     next_pos = (move_x, move_y)

    #     # Move to the next position
    #     # if self.model.grid.is_cell_empty(next_pos):
    #     self.model.grid.move_agent(self, next_pos)
    #     print(f"{self.unique_id} moved to {next_pos}.")   #next.pos -> only for calculations



#     # def calculate_distance(pos1, pos2):
#     #     """Calculate Manhattan distance between two points."""
#     #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])




#############################################################
           ### Move Towards Crop (picker) - Extended - test for reach pick
#############################################################

    
    def move_towards(self, target_pos):
     """
     Move toward the closest accessible grid near the target crop.
     """
     from model import TreeAgent

     # Get all reachable positions around the target crop
     reachable_positions = [
         pos for pos in self.Reach
         if not any(isinstance(agent, TreeAgent) for agent in self.model.grid.get_cell_list_contents(pos))
     ]

     # If no reachable positions exist, return
     if not reachable_positions:
         print(f"Picker {self.unique_id} cannot find a reachable position near the crop at {target_pos}.")
         return

     # Choose the closest position to the target crop
     closest_pos = min(
         reachable_positions, key=lambda pos: abs(pos[0] - target_pos[0]) + abs(pos[1] - target_pos[1])
     )

     # Calculate the next step toward the closest position
     current_x, current_y = self.pos
     target_x, target_y = closest_pos
     dx = target_x - current_x
     dy = target_y - current_y
     next_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
     next_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
     next_position = (next_x, next_y)

     # Move the picker to the next position, as long as it's not obstructed by a tree
     if not any(isinstance(agent, TreeAgent) for agent in self.model.grid.get_cell_list_contents(next_position)):
         self.model.grid.move_agent(self, next_position)
         print(f"Picker {self.unique_id} moved to {next_position}.")
     else:
         print(f"Picker {self.unique_id} could not move to {next_position} due to a tree.")





#     # def calculate_distance(pos1, pos2):
#     #     """Calculate Manhattan distance between two points."""
#     #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


#########################################################################################################################################################


##class ExtendedDroneRobot: