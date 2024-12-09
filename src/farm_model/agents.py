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


# ############################################################
#     ##### Drones Class Initialisation ( Main Class ) 
# #############################################################

# class DroneRobot(Agent):
#     """
#     Drone in the farm 
#     """


#     def __init__(self, unique_id, pos, model):
#         print(f"Initialising the drone robot with {unique_id}, {pos}, {model}")
#         super().__init__(unique_id, model)
#         self.pos = pos
#         self.state = "idle"      ## "idle" or "searching"
#         self.battery =  100
#         self.battery_tick = 0
#         self.type =  "drone_robot"
#         #for dynamic arrow 
#         self.prev_pos = pos # Track previous position ( # for dynamic heading )
#         self.heading = (0,0)

#     # # for  dynamic arrowhead ##
#     # def arrow_step(self):
#     #     # Update position and heading
#     #     self.prev_pos = self.pos
#     #     # Example movement logic (replace with your actual logic)
#     #     self.pos = (self.pos[0] + 1, self.pos[1])
#     #     self.heading = (self.pos[0] - self.prev_pos[0], self.pos[1] - self.prev_pos[1])


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
#         print(f"Drone {self.unique_id}: Prev Pos = {self.prev_pos}, Current Pos = {self.pos}, Heading = {self.heading}")




    
#     @property 
#     def is_busy(self):
#         return self.state == BUSY
    
#         #####################################
#            ### Move Randomly function (Drones)
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
#            ### Check for Crops function (Drones)
#         ######################################


#     def check_for_crop(self):
#         """
#         Check if the current cell contains a CropAgent (strawberries ) 
#         """
#         from model import CropAgent    #avoid cicular import 
#         for agent in self.model.grid.get_cell_list_contents(self.pos):
#             if isinstance(agent, CropAgent):
#                 print(f"DroneRobot {self.unique_id} found a crop at {self.pos}")
#                 return True
#         return False
        


#         ######################################
#            ### Step Function (Drones)
#         ######################################

#     def step(self):
#         """ 
#         Define the action of drones at each step 
#         """
#         print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}")

        
#         ##Decrease battery 
#         self.battery_tick += 1

#         if self.battery_tick >= 50:  ## can adjust the threshold here , or use the same one as picker at the top  # 500 steps
#             self.battery_tick =  0
#             self.battery -= 1 


#         #stop if battery is run out 
#         if self.battery <= 90:
#             print (f"Drone {self.unique_id} has run out of battery and is stopping at {self.pos}.")
#             #return 
#             self.return_to_base()
        


#         #check for crops
#         if self.check_for_crop():
#             print(f"DroneRobot {self.unique_id} is reporting a crop at {self.pos}.")
#             #pause for a moment (simulate reporting a crop)
#             return 
        
#         ####   TODO : two drones at one crop ? 

#         #move randomly if no crop is found 
#         self.move_randomly()


#         #update position and heading dynamically (optional for dynamic arrowhead)
#         self.arrow_step()



#         ######################################
#            ### Return to bsae Function (Drones) Working 
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
    ##### Drones Classsss for signal test 
#############################################################

class DroneRobot(Agent):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = "searching"  # "searching" or "returning"
        self.battery = 100
        self.battery_tick = 0
        self.type = "drone_robot"
        self.signal_queue = []  # To store crop locations to signal pickers
        self.picker_id_waiting = None


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

        # Look for crops
        if self.check_for_crop():
            print(f"Drone {self.unique_id} found a crop at {self.pos}. Signaling picker.")
            self.signal_picker()
            self.state = "waiting"
            return

        # Move randomly if no crop is found
        self.move_randomly()
        
        
        
        
        ####### -----------------------
        
        

    def check_for_crop(self):
        """
        Check if the current cell contains a CropAgent (strawberries).
        """
        from model import CropAgent  # Avoid circular import
        for agent in self.model.grid.get_cell_list_contents(self.pos):
            if isinstance(agent, CropAgent):
                print(f"DroneRobot {self.unique_id} found a crop at {self.pos}")
                return True
        return False


### utility function to calculate the distance 
    # def get_distance(pos1, pos2):
    #     """Calculate Manhattan distance between two points."""
    #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    

    # def signal_picker(self):
    #     """
    #     Signal pickers at the base about the crop location.
    #     """
    #     from agents import PickerRobot

    #     pickers = [
    #         agent for agent in self.model.schedule.agents
    #         if isinstance(agent, PickerRobot) and agent.state == "waiting"
    #     ]

    #     if not pickers:
    #         print(f"No pickers available to signal.")
    #         return

    #     # Find the nearest picker
    #     nearest_picker = min(
    #         pickers, key=lambda picker: self.model.grid.get_distance(self.pos, picker.pos)
    #     )

    #     # Assign crop location to the picker
    #     nearest_picker.target_pos = self.pos
    #     nearest_picker.state = "moving_to_crop"
    #     print(f"Drone {self.unique_id} signaled Picker {nearest_picker.unique_id} to move to {self.pos}.")

    ### -----------------------------------------------------------------------
    
    
    def signal_picker(self):
        """
        Signal pickers at the base about the crop location.
        """
        from agents import PickerRobot

        # Find pickers in the "waiting" state
        pickers = [
            agent for agent in self.model.schedule.agents
            if isinstance(agent, PickerRobot) and agent.state == "waiting"
        ]

        if not pickers:
            print(f"No pickers available to signal.")
            return

        # Calculate Manhattan distance between the drone and each picker
        def manhattan_distance(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        # Find the nearest picker using the Manhattan distance
        nearest_picker = min(
            pickers, key=lambda picker: manhattan_distance(self.pos, picker.pos)
        )

        # Assign crop location to the nearest picker
        nearest_picker.target_pos = self.pos
        nearest_picker.state = "moving_to_crop"
        self.picker_id_waiting = nearest_picker.unique_id
        print(f"Drone {self.unique_id} signaled Picker {nearest_picker.unique_id} to move to {self.pos}.")





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
    def calculate_distance(pos1, pos2):
        """Calculate Manhattan distance between two points."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    


# ############################################################################################################
#            ## PickerRobot Class Initialisation (Main Class)
# ############################################################################################################


# class PickerRobot(Agent):
#     """ 
#     Picker robot in the farm
#     """
    
    
#     def __init__(self, unique_id, pos, model):    # , init_state= FREE
#         print(f"Initializing the picker robot with {unique_id}, {pos}, {model}")    # debug print for checking picker robot is placed at the desied locaton with defined arguments
#         super().__init__(unique_id, model)
#         self.pos = pos
#         self.state = FREE  #FREE as default
#         self.storage = 0  #number of strawberries carred , 0 at initial stage
#         self.capacity = 1000  # maximum storage capacity 
#         self.battery = 100    #placeholder for the battery threadhold
#         self.battery_tick = 0
#         self.type = "picker_robot"
#         self.step_count = 0    #initialise the step counter 

#         #TODO : CAPACITY CHECK
        

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
    

#     @property 
#     def is_busy(self):
#         return self.state == BUSY
    

# #############################################################
#            ### step function (picker )
# #############################################################
    
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





# #############################################################
#            ### Make Decison Function(picker) 
# #############################################################
  
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
   
   
# #############################################################
#            ### Move Randomly function (picker)
# #############################################################
    
    
        
#     def move_randomly(self):    # responbile for moving the robot 
#         """ 
#         Move the robot to a random neighboring cell, avoiding trees , Reduce speed when moving through water
#         """
#         from model import TreeAgent, WaterAgent
#         #from model import CropAgent
#         # imported locally only before they are called / if imported globally at the top, it is circulr dependency with model.py

#         # slowing down for moving through water
#         if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0 :
#             print(f"PickerRobot {self.unique_id} is slowing down near the water")
#             self.slowdown_counter -= 1 
#             return   # skip  this step 


#         possible_steps = self.model.grid.get_neighborhood(
#             self.pos, moore = True, include_center=False
#         )
#         valid_steps = [ step for step in possible_steps if not any(isinstance (a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))] 
#         # valid_steps = [
#         #     step for step in possible_steps
#         # #     if self.model.grid.is_cell_empty(step)   #check if the cell is empty 
#         # #     and not any(isinstance(a,TreeAgent) for a in self.model.grid.get_cell_list_contents(step))     #avoid trees
#         #        ##instead of checking ...... 
#         #     if not any(isinstance(a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))
#         # ]
#         print(f"PickerRobot {self.unique_id} valid steps: {valid_steps}")    # debugging 
#         if valid_steps:
#             #move to a randomly chosen valid step 
#             new_position = self.random.choice(valid_steps)
#             print(f"PickerRobot {self.unique_id} moving from {self.pos} to {new_position}.")


#             #slowing down moving through river 
#             if any(isinstance (a, WaterAgent) for a in self.model.grid.get_cell_list_contents(new_position)):
#                 print ("Picker Robot {self.unique_id} entering water at {self.position}.")
#                 self.slowdown_counter = 5     #slow down for 5 steps 
#             self.model.grid.move_agent(self, new_position)
#             print(f"PickerRobot {self.unique_id} moved to {new_position}")     #debug 
            


# #############################################################
#            ### Pick Function for PickerRobots
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



# #############################################################
#            ### Return To Base function (picker) Working 
# #############################################################            
           
# ##   from collections import deque
#     ######  working working  #### 
#     def return_to_base(self):
#        """
#        Move toward the base to drop off crops, avoiding trees and slowing down in water.
#        Uses BFS to find a valid path to the base.
#        """
#        print(f"Picker Robot is returning to base at Step: {self.step_count}")
#        from model import TreeAgent, WaterAgent
       

#        # Define the base coordinates
#        base_x, base_y = 0, 0  # Assuming base is at (0, 0)
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



#############################################################
           ### Wait function (picker)
#############################################################
            
    def wait(self):
        """
        wait in place when its not full capacity or nothing to do 
        """
        pass
    

############################################################


    # class name (inheriting from name):
# class SuperPicker(PickerRobot):
    
#     def __init__(self, unique_id, pos, model):
#         super().__init__(unique_id, pos, model)



#############################################################################################################
           ### PickerRobot Class Initialisation (Test for Signalling )
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
        self.target_crop = None  # Crop location to move toward

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
            if self.pos == self.target_pos:
                print(f"Picker {self.unique_id} has arrived at {self.target_pos}. Starting to pick.")
                self.state = "picking"
            else:
                self.move_towards(self.target_pos)  # Move towards the target crop
                return      ############## one picker following the first one 

        # Picking crops
        if self.state == "picking":
            print(f"Picker {self.unique_id} is picking crops.")
            self.pick()
            if self.storage >= self.capacity:  # Return to base if full
                print(f"Picker {self.unique_id} is full. Returning to base.")
                self.state = "returning"
            return

        # Default state: waiting for a signal at the base
        if self.state == "waiting":
            print(f"Picker {self.unique_id} is waiting at the base.")




    def receive_signal(self, crop_location):
        """
        Receive crop location signal from a drone.
        """
        print(f"PickerRobot {self.unique_id} received crop location: {crop_location}")
        self.state = "moving"
        self.target_crop = crop_location

    def move_toward_target(self):
        """
        Move toward the target crop location.
        """
        if self.target_crop:
            current_x, current_y = self.pos
            target_x, target_y = self.target_crop
            dx = target_x - current_x
            dy = target_y - current_y
            next_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
            next_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
            next_position = (next_x, next_y)
            print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_position}")
            self.model.grid.move_agent(self, next_position)

    def pick(self):
        """
        Pick crops at the current position.
        """
        from model import CropAgent
        for agent in self.model.grid.get_cell_list_contents(self.pos):
            if isinstance(agent, CropAgent):
                print(f"Picker {self.unique_id} picked a crop at {self.pos}.")
                self.model.grid.remove_agent(agent)
                self.storage += 1
                self.state = "waiting"
            else:
                self.state = "waiting"


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


    def return_to_base(self):
       """
       Move toward the base to drop off crops, avoiding trees and slowing down in water.
       Uses BFS to find a valid path to the base.
       """
       from model import TreeAgent, WaterAgent

       # Define the base coordinates
       base_x, base_y = 0, 0  # Assuming base is at (0, 0)
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



    def wait(self):
        """
        wait in place when its not full capacity or nothing to do 
        """
        pass


    def move_towards(self, target_pos):
        """
        Move towards the target position.
        """
        current_x, current_y = self.pos
        target_x, target_y = target_pos

        # Calculate the direction
        dx = target_x - current_x
        dy = target_y - current_y
        move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
        move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
        next_pos = (move_x, move_y)

        # Move to the next position
        # if self.model.grid.is_cell_empty(next_pos):
        self.model.grid.move_agent(self, next_pos)
        print(f"{self.unique_id} moved to {next_pos}.")



#     # def calculate_distance(pos1, pos2):
#     #     """Calculate Manhattan distance between two points."""
#     #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


#########################################################################################################################################################


##class ExtendedDroneRobot: