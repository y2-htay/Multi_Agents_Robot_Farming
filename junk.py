############ From Agents Py ##########################

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




##################################################################################################