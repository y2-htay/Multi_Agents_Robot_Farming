# ##################################################################
#          #"""Drone Class ---   Main One with Make Decision"""  still testing 
# ##################################################################
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
