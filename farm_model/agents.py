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


############################################################
    ##### Drones Class Initialisation
#############################################################

class DroneRobot(Agent):
    """
    Drone in the farm 
    """


    def __init__(self, unique_id, pos, model):
        print(f"Initialising the drone robot with {unique_id}, {pos}, {model}")
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = "idle"      ## "idle" or "searching"
        self.battery =  100
        self.battery_tick = 0
        self.type =  "drone_robot"
        #for dynamic arrow 
        self.prev_pos = pos # Track previous position ( # for dynamic heading )
        self.heading = (0,0)

    # # for  dynamic arrowhead ##
    # def arrow_step(self):
    #     # Update position and heading
    #     self.prev_pos = self.pos
    #     # Example movement logic (replace with your actual logic)
    #     self.pos = (self.pos[0] + 1, self.pos[1])
    #     self.heading = (self.pos[0] - self.prev_pos[0], self.pos[1] - self.prev_pos[1])


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
        print(f"Drone {self.unique_id}: Prev Pos = {self.prev_pos}, Current Pos = {self.pos}, Heading = {self.heading}")




    
    @property 
    def is_busy(self):
        return self.state == BUSY
    
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
           ### Check for Crops function (Drones)
        ######################################


    def check_for_crop(self):
        """
        Check if the current cell contains a CropAgent (strawberries ) 
        """
        from model import CropAgent    #avoid cicular import 
        for agent in self.model.grid.get_cell_list_contents(self.pos):
            if isinstance(agent, CropAgent):
                print(f"DroneRobot {self.unique_id} found a crop at {self.pos}")
                return True
        return False
        


        ######################################
           ### Step Function (Drones)
        ######################################

    def step(self):
        """ 
        Define the action of drones at each step 
        """
        print(f"DroneRobot {self.unique_id} at position {self.pos} with battery {self.battery}")

        
        ##Decrease battery 
        self.battery_tick += 1

        if self.battery_tick >= 50:  ## can adjust the threshold here , or use the same one as picker at the top  # 500 steps
            self.battery_tick =  0
            self.battery -= 1 


        #stop if battery is run out 
        if self.battery <= 90:
            print (f"Drone {self.unique_id} has run out of battery and is stopping at {self.pos}.")
            #return 
            self.return_to_base()
        


        #check for crops
        if self.check_for_crop():
            print(f"DroneRobot {self.unique_id} is reporting a crop at {self.pos}.")
            #pause for a moment (simulate reporting a crop)
            return 
        
        ####   TODO : two drones at one crop ? 

        #move randomly if no crop is found 
        self.move_randomly()


        #update position and heading dynamically (optional for dynamic arrowhead)
        self.arrow_step()



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
        


#############################################################
           ### PickerRobot Class Initialisation
#############################################################


class PickerRobot(Agent):
    """ 
    Picker robot in the farm
    """
    
    
    def __init__(self, unique_id, pos, model):    # , init_state= FREE
        print(f"Initializing the picker robot with {unique_id}, {pos}, {model}")    # debug print for checking picker robot is placed at the desied locaton with defined arguments
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = FREE  #FREE as default
        self.storage = 0  #number of strawberries carred , 0 at initial stage
        self.capacity = 1000  # maximum storage capacity 
        self.battery = 100    #placeholder for the battery threadhold
        self.battery_tick = 0
        self.type = "picker_robot"

        #TODO : CAPACITY CHECK
        

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
    

    @property 
    def is_busy(self):
        return self.state == BUSY
    

# #############################################################
#            ### step function (picker )
# #############################################################
    
    def step(self):
        """ 
        Define the behaviour of the robot at each step 
        """
        print(f"PickerRobot {self.unique_id} is stepping at position {self.pos}.")
        print("battery for ", self.unique_id, " = ", self.battery)
        print("Storage for", self.unique_id, "=", self.storage)

        
        #decrease battery level every few ticks 
        self.battery_tick += 1
        
        if self.battery_tick == BATTERY_SKIP_THRESHOLD:
            self.battery_tick = 0
            self.battery -= 1
            
        
        print(f"PickerRobot {self.unique_id} is taking a step at position {self.pos}.") #debug
        #Decision making 
        action = self.make_decision()
        print(f"PickerRobot {self.unique_id} decided to : {action }")     #debug print for the visual movement of pickerrobot 
        getattr(self,action)()        #execuse the chosen action 





# #############################################################
#            ### Make Decison Function(picker) 
# #############################################################
  
    def make_decision(self):
      """
      Decide the next action based on the robot's state and surroundings.
      """
      print(f"PickerRobot {self.unique_id} is making a decision.")
      from model import CropAgent

      # If the battery is depleted, return to base
      if self.battery <= 90:
          print(f"PickerRobot {self.unique_id} battery died. Returning to base.")
          self.state = "returning"  # added states
          return "return_to_base"   # return to base instead of wait 

      # If storage is full, transition to "returning" state and return to base
      if self.storage >= 1000:
          print(f"PickerRobot {self.unique_id} storage is full. Returning to base.")
          self.state = "returning"  ## added states 
          return "return_to_base"   ## return to base instead of wait 

      # If in "returning" state, continue heading back to the base, confirming it to go to base 
      if self.state == "returning":
          return "return_to_base"

      # If free, check for nearby crops
      if self.state == FREE:
          crop_nearby = any(
            isinstance(agent, CropAgent)
            for agent in self.model.grid.get_neighbors(self.pos, moore=True, include_center=False, radius=3)
        )
          print(f"PickerRobot {self.unique_id} Crop Nearby: {crop_nearby}")
          if crop_nearby:
              return "pick"
          else:
              return "move_randomly"

      # Default fallback
      return "wait"
   
   
#############################################################
           ### Move Randomly function (picker)
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
           ### Pick Function for PickerRobots
#############################################################
    
            
    def pick(self):
        """ 
        Pick the strawberry if one is in the current cell
        """
        print(f"Hey I am ready to pickkkkkkkkkk the strawberry ")
        from model import CropAgent     #imported locally 
        
        reachable = self.Reach
        
        print("reachable", reachable)
        
        for each in self.Reach:
            print("Checking, ", each)
            
            for agent in self.model.grid.get_cell_list_contents(each):
                if isinstance(agent, CropAgent):
                    print(f"PickerRobot {self.unique_id} found a strawberry at {each}")
                    self.model.grid.remove_agent(agent)
                    self.model.schedule.remove(agent)
                    self.storage += 1
                    print("successfully picked at: ", each, "  Storage: ", self.storage)
                    continue
                print("Not a crop")



#############################################################
           ### Return To Base function (picker) Working 
#############################################################            
           
##   from collections import deque
    ######  working working  #### 
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
