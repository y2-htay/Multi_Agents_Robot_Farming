### extened after all deliberate is fixed




# import warnings
# warnings.filterwarnings("ignore", category  = FutureWarning)
# import mesa
# from mesa import Agent
# import heapq
# from collections import deque


# #from .model import FREE, BUSY
# #from model import TreeAgent, CropAgent

# BATTERY_SKIP_THRESHOLD = 5   # picker - change thereadshold 

# #defining the constants for states
# FREE = 1         #picker
# BUSY = 0         #picker


# ############################################################
#     ##### Drones Classsss (signal + aging ) Extended , Basic 
# #############################################################


# class DroneRobot(Agent):
#     """Drone in the Farm """
#     def __init__(self, unique_id, pos, model):
#         super().__init__(unique_id, model)
#         self.pos = pos
#         self.state = "searching"  # "searching" or "returning"
#         self.battery = 100
#         self.battery_tick = 0
#         self.type = "drone_robot"
#         #for dynamic arrow 
#         self.prev_pos = pos # Track previous position ( # for dynamic heading )
#         self.heading = (0,0)        
#         self.signal_queue = []  # To store crop locations to signal pickers
#         self.picker_id_waiting = None


#     ######################################
#     ### Arrow Step (Drone)
#     ######################################



#     # Dynamic Arrowhead (new )
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
#         #print(f"Drone {self.unique_id}: Prev Pos = {self.prev_pos}, Current Pos = {self.pos}, Head



#     ######################################
#     ### Property - is_busy (Drone)
#     ######################################


#     @property 
#     def is_busy(self):
#         return self.state == BUSY




#     ######################################
#     ### Step Function (Drone) Extended -- stepmakedecision working 
#     ######################################


#     def step(self):
#         """
#         Define the behavior of drones at each step.
#         """
#         print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}.")

#         # Make a decision and execute the corresponding action
#         action, arg = self.make_decision()
#         if hasattr(self, action):  # Safeguard against invalid actions
#             if arg is not None:
#                 getattr(self, action)(arg)  # Call the method with an argument
#             else:
#                 getattr(self, action)()  # Call the method without arguments
#             print(f"Drone {self.unique_id} executed: {action}.")
#         else:
#             print(f"Error: Drone {self.unique_id} does not have a valid action '{action}'.")



#     ######################################
#     ### Make Decision Function (Drone) Extended -- stepmakedecision working 
#     ######################################



#     def make_decision(self):
#         """
#         Decide the next action based on the drone's state, battery, and surroundings.
#         """
#         print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}.")

#         # Decrease battery over time
#         self.battery_tick += 1
#         if self.battery_tick >= 50:  # Adjust this threshold as needed
#             self.battery_tick = 0
#             self.battery -= 1

#         # Return to base if battery is low
#         if self.battery <= 20:
#             print(f"Drone {self.unique_id} has low battery and is returning to base.")
#             self.state = "returning"
#             self.arrow_step()  # Ensure arrow updates during movement
#             return "return_to_base", None

#         # If waiting for a picker to arrive
#         if self.state == "waiting":
#             print(f"Drone {self.unique_id} is waiting for a picker {self.picker_id_waiting} at {self.pos}.")
#             if not self.check_for_crop():
#                 self.state = "searching"
#             # Check if a picker has arrived
#             if any(
#                 isinstance(agent, PickerRobot) and agent.pos == self.pos
#                 for agent in self.model.grid.get_cell_list_contents(self.pos)
#             ):
#                 print(f"Picker has arrived at {self.pos}. Drone {self.unique_id} will resume searching.")
#                 self.state = "searching"
#             self.arrow_step()  # Arrow may change when waiting ends
#             return "wait", None

#         # Look for crops
#         if self.check_for_crop():
#             print(f"Drone {self.unique_id} found a crop at {self.pos}. Signaling picker.")
#             self.state = "waiting"
#             self.arrow_step()  # Arrow adjusts when signaling
#             return "signal_picker", None

#         # Move randomly if no crop is found
#         self.arrow_step()  # Arrow adjusts with random movement
#         return "move_randomly", None


        

#     ######################################
#     ### Check for crop ( Drone ) Basic + Extended 
#     ######################################


#     def check_for_crop(self):
#         """ Check for mature crop to signal to the pickers"""
#         from model import CropAgent   #avoid circular import 
#         for agent in self.model.grid.get_cell_list_contents(self.pos):
#             if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
#                 print(f"Drone {self.unique_id} has found a mature crop at {self.pos}")
#                 return True
#         return False



#     ######################################
#     ### Signal Picker (Drone) Extended 
#     ######################################


#     ## updated one with the crop stage check in check_for_crop()
#     def signal_picker(self):
#         """
#         Signal pickers at the base about the crop location.
#         """
#         print(f"Drone bout to signal pickerssss ")
#         from agents import PickerRobot

#         # Find pickers in the "waiting" state
#         pickers_to_signal = [
#             agent for agent in self.model.schedule.agents
#             if isinstance(agent, PickerRobot) and agent.state == "waiting"
#         ]

#         if not pickers_to_signal:
#             print(f"No pickers available to signal.")
#             return

#         # Calculate Manhattan distance between the drone and each picker
#         def manhattan_distance(pos1, pos2):
#             return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

#         # Find the nearest picker using the Manhattan distance
#         nearest_picker = min(
#             pickers_to_signal, key=lambda picker: manhattan_distance(self.pos, picker.pos)
#         )

#         # Assign crop location to the nearest picker
#         nearest_picker.target_pos = self.pos  # change here with the reach, cant overlap on the tree grid
#         nearest_picker.state = "moving_to_crop"   
#         self.picker_id_waiting = nearest_picker.unique_id
#         print(f"Drone {self.unique_id} signaled Picker {nearest_picker.unique_id} to move to {self.pos}.")




#         #####################################
#            ### Move Randomly function (Drones) Basic + Extended 
#         ######################################
    
#     def move_randomly(self):
#         """
#         Move the drone to a random neighboring cell, ignoring all terrain constraint restrictions 
#         """
#         possible_steps = self.model.grid.get_neighborhood(
#             self.pos , moore = False, include_center = False, radius=1
#         )
#         new_position = self.random.choice (possible_steps)
#         print (f"DroneRobot {self.unique_id} moving from {self.pos} to {new_position} .")
#         self.prev_pos = self.pos
#         self.model.grid.move_agent(self, new_position)



#         ######################################
#            ### Return to bsae Function (Drones) Basic + Extended 
#         ######################################
        
#     def return_to_base(self):
#             """
#             Move directly toward the base to drop off crops or recharge, without avoiding trees or slowing down in water.
#             """
#             # Define the base coordinates
#             base_x, base_y = 0, 0  # Assuming base is at (0, 0)
#             base_position = (base_x, base_y)

#             # If the drone is already at the base, stop
#             if self.pos == base_position:
#                 print(f"DroneRobot {self.unique_id} has reached the base at {self.pos}.")
#                 return

#             # Determine the direction to the base
#             current_x, current_y = self.pos
#             dx = base_x - current_x
#             dy = base_y - current_y

#             # Calculate the next step toward the base
#             move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
#             move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
#             next_position = (move_x, move_y)

#             # Move to the next position
#             print(f"DroneRobot {self.unique_id} moving from {self.pos} to {next_position}.")
#             self.model.grid.move_agent(self, next_position)


# ##############################################################################################################


#     # class name (inheriting from name):
# # class SuperPicker(PickerRobot):
    
# #     def __init__(self, unique_id, pos, model):
# #         super().__init__(unique_id, pos, model)



# #############################################################################################################
#            ### PickerRobot Class Initialisation  ( Basic + Extended)
# #############################################################################################################

# class PickerRobot(Agent):
#     def __init__(self, unique_id, pos, model):
#         super().__init__(unique_id, model)
#         self.pos = pos
#         self.state = "waiting"  # States: "waiting", "moving", "picking", "returning"
#         self.storage = 0
#         self.capacity = 1000
#         self.battery = 100
#         self.battery_tick = 0
#         self.type = "picker_robot"
#         self.target_crop = None  # Crop location to move toward target crop


# #############################################################
#            ### Reach - Property (picker ) - Basic + Extended 
# #############################################################


#     #reach property checking positions only inside the grid. 
#     @property
#     def Reach(self) -> list:
#         positions = []
#         c_x , c_y  =self.pos
#         for x in range (-3,4):
#             for y in range(-3, 4):
#                 #check if the reach is accessing the positions outside of the grid , 
#                 if 0 <= c_x + x < self.model.grid.width and 0<= c_y + y < self.model.grid.height:
#                     positions.append((c_x + x , c_y + y ))
#         return positions



# #############################################################
#            ### is_busy - Property (picker ) - Basic + Extended
# #############################################################

#     @property 
#     def is_busy(self):
#         return self.state == BUSY





# #############################################################
#            ### Step function (picker ) - Extended ( with signalling )  working - stepmakedecison fixed 
# #############################################################

#     def step(self):
#         """
#         Define the behavior of pickers at each step.
#         """
#         print(f"PickerRobot {self.unique_id} at position {self.pos} with storage {self.storage} and battery {self.battery}.")

#         # Decrease battery over time
#         self.battery_tick += 1
#         if self.battery_tick >= 50:  # Adjust this threshold as needed
#             self.battery_tick = 0
#             self.battery -= 1

#         # Check for battery or storage constraints
#         if self.battery <= 20 or self.storage >= self.capacity:
#             print(f"Picker {self.unique_id} is returning to base (battery or storage issue).")
#             self.return_to_base()
#             return

#         # Make a decision and execute the corresponding action
#         action, arg = self.make_decision()
#         if hasattr(self, action):  # Safeguard against invalid actions
#             if arg is not None:
#                 getattr(self, action)(arg)  # Call the method with an argument
#             else:
#                 getattr(self, action)()  # Call the method without arguments
#             print(f"Picker {self.unique_id} executed: {action}.")
#         else:
#             print(f"Error: Picker {self.unique_id} does not have a valid action '{action}'.")

 





# #############################################################
#            ### Notes - Workflow  (picker) - Extended
# #############################################################


# # ## work flow for pickers 
# # check battery and storage ,  -> not ok, retur to BaseException

# # if moving to signaled crop, 
# #     state-> moving to crop
# #     if picker reach target position (self.target.pos)
# #       state-> switch to picking 
# # otherwise ---> move towareds to crop 



# # if picking crops ( state-> picking)
# #     continute picking until storage is full
# #     if storage full , then return to base 


# # if waiting at the base, (state -> waiting)
# #     stay idle and wait for the signal










# #############################################################
#            ### Make Decision (picker) ( Extended ) With Signalling --- working - stepmakedecison fixed 
# #############################################################

#     def make_decision(self):
#         """
#         Decide the next action based on the robot's state, battery, storage, and surroundings.
#         """
#         print(f"PickerRobot {self.unique_id} at position {self.pos} with storage {self.storage} and battery {self.battery}.")

#         # Check for battery or storage constraints first
#         if self.battery <= 20:
#             print(f"PickerRobot {self.unique_id} battery low. Returning to base.")
#             self.state = "returning"
#             return "return_to_base", None

#         if self.storage >= self.capacity:
#             print(f"PickerRobot {self.unique_id} storage full. Returning to base.")
#             self.state = "returning"
#             return "return_to_base", None

#         # Handle state transitions and decide next action
#         if self.state == "waiting":
#             print(f"PickerRobot {self.unique_id} is waiting at the base.")
#             return "wait", None

#         if self.state == "moving_to_crop":
#             print(f"PickerRobot {self.unique_id} is moving to a crop at {self.target_pos}.")
#             if self.pos == self.target_pos:
#                 print(f"PickerRobot {self.unique_id} has arrived at {self.target_pos}. Starting to pick.")
#                 self.state = "picking"
#                 return "pick", None
#             else:
#                 return "move_towards", self.target_pos

#         if self.state == "picking":
#             print(f"PickerRobot {self.unique_id} is picking crops.")
#             if self.storage < self.capacity:
#                 return "pick", None
#             else:
#                 print(f"PickerRobot {self.unique_id} is full. Returning to base.")
#                 self.state = "returning"
#                 return "return_to_base", None

#         if self.state == "returning":
#             print(f"PickerRobot {self.unique_id} is returning to base.")
#             return "return_to_base", None

#         # Default fallback action
#         print(f"PickerRobot {self.unique_id} is in an unrecognized state: {self.state}. Defaulting to 'wait'.")
#         return "wait", None

        













# #############################################################
#            ### Receive Signal (picker) - Extended
# #############################################################

#     def receive_signal(self, crop_location):
#         """
#         Receive crop location signal from a drone.
#         """
#         print(f"PickerRobot {self.unique_id} received crop location: {crop_location}")
#         self.state = "moving"      ##moving randomly ??
#         self.target_crop = crop_location  # assigned here 



# #############################################################
#            ### Pick (Picker) - Extended - (aging)
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
            

# # # self.state = "waiting"
# # #             else:
# # #                 self.state = "waiting"














# #############################################################
#            ### Return To Base (picker) Basic + Extended 
# #############################################################  


#     def return_to_base(self):
#        """
#        Move toward the base to drop off crops, avoiding trees and slowing down in water.
#        Uses BFS to find a valid path to the base.
#        """
#        from model import TreeAgent, WaterAgent

#        # Define the base coordinates
#        base_x, base_y = 0, 0  # Assuming base is at (0, 0)   ## need to fix for new base position 
#        base_position = (base_x, base_y)

#        # If the robot is already at the base, stop
#        if self.pos == base_position:
#            print(f"PickerRobot {self.unique_id} has reached the base at {self.pos}.")
#            return

#        # BFS setup to find the shortest path to the base
#        queue = deque([(self.pos, [])])  # (current position, path taken)
#        visited = set()  # To avoid revisiting nodes
#        visited.add(self.pos)

#        while queue:
#            current_pos, path = queue.popleft()

#            # Check the current position for base
#            if current_pos == base_position:
#                # Follow the first step in the path to move toward the base
#                if path:
#                    next_step = path[0]

#                    # Check for water slowdown
#                    if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0:
#                        print(f"PickerRobot {self.unique_id} is slowing down near the water.")
#                        self.slowdown_counter -= 1
#                        return  # Skip this step

#                    if any(isinstance(a, WaterAgent) for a in self.model.grid.get_cell_list_contents(next_step)):
#                        print(f"PickerRobot {self.unique_id} entering water at {next_step}.")
#                        self.slowdown_counter = 5  # Slow down for 5 steps

#                    # Move to the next step
#                    print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_step}.")
#                    self.model.grid.move_agent(self, next_step)
#                return

#            # Explore neighbors
#            possible_steps = self.model.grid.get_neighborhood(current_pos, moore=True, include_center=False)
#            for step in possible_steps:
#                # Avoid revisiting and avoid trees
#                if step not in visited and not any(isinstance(a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step)):
#                    visited.add(step)
#                    queue.append((step, path + [step]))

#        print(f"PickerRobot {self.unique_id} could not find a path to the base from {self.pos}.")



# #############################################################
#            ### Wait function (picker) - Basic + Extended 
# #############################################################

#     def wait(self):
#         """
#         wait in place when its not full capacity or nothing to do 
#         """
#         pass



# #############################################################
#            ### Move Towards Crop (picker) - Extended 
# #############################################################


#     def move_towards(self, target_pos):    # target pos,(called in picker step)
#         """
#         Move towards the target position.
#         """
#         current_x, current_y = self.pos
#         target_x, target_y = target_pos

#         # Calculate the direction
#         dx = target_x - current_x
#         dy = target_y - current_y
#         move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
#         move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
#         next_pos = (move_x, move_y)

#         # Move to the next position
#         # if self.model.grid.is_cell_empty(next_pos):
#         self.model.grid.move_agent(self, next_pos)
#         print(f"{self.unique_id} moved to {next_pos}.")   #next.pos -> only for calculations



# #########################################################################################################################################################


# ##class ExtendedDroneRobot: