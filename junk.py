##################################################################################################
############ From Agents Py ##########################
##################################################################################################









##################################################################################################

#     # def calculate_distance(pos1, pos2):
#     #     """Calculate Manhattan distance between two points."""
#     #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])



##################################################################################################



#############################################################
           ### Move Towards Crop (picker) - Extended - test for reach pick
#############################################################


    # def move_towards(self, target_pos):
    #  """
    #  Move toward the closest accessible grid near the target crop.
    #  """
    #  from model import TreeAgent

    #  # Get all reachable positions around the target crop
    #  reachable_positions = [
    #      pos for pos in self.Reach
    #      if not any(isinstance(agent, TreeAgent) for agent in self.model.grid.get_cell_list_contents(pos))
    #  ]

    #  # If no reachable positions exist, return
    #  if not reachable_positions:
    #      print(f"Picker {self.unique_id} cannot find a reachable position near the crop at {target_pos}.")
    #      return

    #  # Choose the closest position to the target crop
    #  closest_pos = min(
    #      reachable_positions, key=lambda pos: abs(pos[0] - target_pos[0]) + abs(pos[1] - target_pos[1])
    #  )

    #  # Calculate the next step toward the closest position
    #  current_x, current_y = self.pos
    #  target_x, target_y = closest_pos
    #  dx = target_x - current_x
    #  dy = target_y - current_y
    #  next_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
    #  next_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
    #  next_position = (next_x, next_y)

    #  # Move the picker to the next position, as long as it's not obstructed by a tree
    #  if not any(isinstance(agent, TreeAgent) for agent in self.model.grid.get_cell_list_contents(next_position)):
    #      self.model.grid.move_agent(self, next_position)
    #      print(f"Picker {self.unique_id} moved to {next_position}.")
    #  else:
    #      print(f"Picker {self.unique_id} could not move to {next_position} due to a tree.")



##################################################################################################

    # ###work flow ( picker)
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
           ### Pick (Picker) - Extended - Still fixing - to pick from reach - test
#############################################################

    # def pick(self):
    #   """
    #   Pick the crop if it is within the picker's reach.
    #   """
    #   print(f"Picker at the nearest place of crop, ready to pick")
    #   from model import CropAgent

    #   # Check all positions in reach for mature crops
    #   for pos in self.Reach:
    #       for agent in self.model.grid.get_cell_list_contents(pos):
    #         if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
    #             print(f"Picker {self.unique_id} picked a crop at {pos}. Resetting to seed stage.")
    #             agent.reset_crop_stage()  # Reset the crop to the seed stage
    #             self.storage += 1
    #             self.state = "waiting"  # Return to waiting state after picking
    #             return

    #   # If no crop is found in reach, continue moving toward the target
    #   print(f"Picker {self.unique_id} found no crop in reach.")
    #   self.state = "moving_to_crop"







#############################################################
           ### Pick (Picker) - Extended - test for pick from reach 
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
           ### Pick (Picker) - Extended - Need to fix - to pick from reach
#############################################################

    # ##  double check here if the grid has  a mature crop and replace it with seed after picking 
    # def pick(self):
    #     """
    #     Pick crops at the current position.
    #     """
    #     from model import CropAgent
    #     for agent in self.model.grid.get_cell_list_contents(self.pos):
    #         if isinstance(agent, CropAgent) and agent.growth_stage == "mature":
    #            print(f"Picker {self.unique_id} picked a crop at {self.pos}. Resetting to seed stage")
    #            agent.reset_crop_stage()  # changed here 
    #            self.storage += 1      #reset to seed stage
    #            self.stage = "waiting"     # return to waiting state after picking
    #         else:
    #             self.state = "waiting"  # this is the problem, dont forget this 
            

# # self.state = "waiting"
# #             else:
# #                 self.state = "waiting"

##################################################################################################


#############################################################
           ### Step function (picker ) - Extended ( with signalling ) - testing for pick from reach 
#############################################################

    # def step(self):
    #  """
    #  Define the behavior of pickers at each step.
    #  """
    #  print(f"PickerRobot {self.unique_id} at position {self.pos} with storage {self.storage} and battery {self.battery}")

    #  # Decrease battery over time
    #  self.battery_tick += 1
    #  if self.battery_tick >= 50:  # Adjust this threshold as needed
    #      self.battery_tick = 0
    #      self.battery -= 1

    #  # Return to base if battery is low or storage is full
    #  if self.battery <= 20 or self.storage >= self.capacity:
    #      print(f"Picker {self.unique_id} is returning to base (battery or storage issue).")
    #      self.return_to_base()
    #      return

    #  # If moving to a signaled crop
    #  if self.state == "moving_to_crop":
    #      print(f"Picker {self.unique_id} is moving to a crop at {self.target_pos}.")
    #      # Check if the picker is within reach of the crop
    #      if self.target_pos and self.pos in self.Reach:
    #          print(f"Picker {self.unique_id} reached the crop within reach. Starting to pick.")
    #          self.state = "picking"  # Transition to picking state
    #      else:
    #          self.move_towards(self.target_pos)  # Move towards the closest reachable grid
    #      return

    #  # Picking crops
    #  if self.state == "picking":
    #      print(f"Picker {self.unique_id} is picking crops.")
    #      self.pick()  # Perform the picking operation
    #      if self.storage >= self.capacity:  # Return to base if full
    #          print(f"Picker {self.unique_id} is full. Returning to base.")
    #          self.state = "returning"
    #      else:
    #          self.state = "waiting"  # Transition to waiting state after picking
    #      return

    #  # Default state: waiting for a signal at the base
    #  if self.state == "waiting":
    #      print(f"Picker {self.unique_id} is waiting at the base.")



##################################################################################################

    #### Adding utility function for drones to move toward the target 

    ### utility function to calculate the distance 
    # def calculate_distance(pos1, pos2):
    #     """Calculate Manhattan distance between two points."""
    #     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


##################################################################################################

        #####################
        ## test for pick from reach, not assigning current positio as their target.pos 
        #####################

    #     # Find all reachable positions around the crop position (drone's position)
    #     from model import TreeAgent
    #     reachable_positions = [
    #        (x, y) for x in range(self.pos[0] - 1, self.pos[0] + 2)
    #        for y in range(self.pos[1] - 1, self.pos[1] + 2)
    #        if 0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height
    #        and not any(isinstance(agent, TreeAgent) for agent in self.model.grid.get_cell_list_contents((x, y)))
    #        and (x, y) != self.pos  # Exclude the drone's current position
    #    ]

    #     if reachable_positions:
    #        # Assign the nearest reachable position as the target
    #        target_position = min(
    #            reachable_positions, key=lambda pos: manhattan_distance(nearest_picker.pos, pos)
    #        )
    #        nearest_picker.target_pos = target_position
    #        nearest_picker.state = "moving_to_crop"
    #        self.picker_id_waiting = nearest_picker.unique_id
    #        print(f"Drone {self.unique_id} signaled Picker {nearest_picker.unique_id} to move to {target_position}.")
    #     else:
    #        print(f"Drone {self.unique_id} found no reachable position for Picker {nearest_picker.unique_id}.")  


############## only for signalling - without crop aging ###########################################

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
##################################################################################################

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


##################################################################################################

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


##################################################################################################


# def move_toward_target(self):
    #     """
    #     Move toward the target crop location.
    #     """
    #     if self.target_crop:
    #         current_x, current_y = self.pos
    #         target_x, target_y = self.target_crop
    #         dx = target_x - current_x
    #         dy = target_y - current_y
    #         next_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
    #         next_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
    #         next_position = (next_x, next_y)
    #         print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_position}")
    #         self.model.grid.move_agent(self, next_position)     # next position( only userd in ), crop_location->  target_crop ( assigned ) , target pos( called in  picker step ) , 



    ######################################
    ### Step Function (Drone) - test for reach pick 
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
        

    #     self.signaled_crop_pos = None  # Add this in the drone's initialization

    #     if self.check_for_crop():
    #         if self.signaled_crop_pos == self.pos:
    #             print(f"Drone {self.unique_id} has already signaled a picker for crop at {self.pos}.")
    #         else:
    #             print(f"Drone {self.unique_id} found a new crop at {self.pos}. Signaling picker.")
    #             self.signal_picker()
    #             self.signaled_crop_pos = self.pos
    #             self.state = "waiting"
    #             return

##################################################################################################
          ##### TODO 
##################################################################################################

### TODO:  Robots making a way back to base in a pattern 
    # Djoikstra's algorithm
    #station name--> tuples()
    #covert the tuples into strings
    #store the hash in place of the station
    #when making the hash, also save the


## TODO: Communication of drones and pickers 

   ## Drones Send signals to picker robots 
   ## individually 
   ## to all pickers 
   ## picker leaves the base once the drone  send a signal with crops coordinates 

## TODO: 
   
    
   
    
  


  ### TODO:  
  ## Stop pickers and robots from going to base unless they need ( storage full or  battery dies)
 
  ## Picker stop when storage is full (Done)

  ## Drone battery dies test (Done)

  ## two drones at one crop #both wait until the picker comes 

  ## dynamic arrowhead for drone (Done)






  ## TODO: Optional 

  ## stages of fruit - no crop, green , yellow , ripe 

  ## check network 

  ## expand the reach ,, neighbors 

  ## make_decision needed in drones ? 

  ## so battery is not based on individual move, its just all about step?

  ## strawberry regrowth 



  ## CHECKLIST : 

  ## Drones move in 6 directions , front , back , left , right , up , down 

  ## Pickers move past water ( reduced speed ? )

  ## 


