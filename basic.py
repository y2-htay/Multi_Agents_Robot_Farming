# ###############################################################
#          #### KEEPING ALL THE FUNCTIONS USED IN BASIC 
# ###############################################################


#         ####################################
#             # PICKER
#         ####################################

# ############################################################
#            ## step function (picker ) - basic- without signalling 
# ############################################################
    
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




# ############################################################
#            ## Make Decison (picker) - ( Basic ) - Without signalling 
# ############################################################
  
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



# ############################################################
#            ## Move Randomly function (picker) - Only Basic
# ############################################################

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



#     # def calculate_distance(pos1, pos2):
#     #     """Calculate Manhattan distance between two points."""
#     #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
