import mesa
from mesa import Agent
#from .model import FREE, BUSY
#from model import TreeAgent, CropAgent



#defining the constants for states
FREE = 1  
BUSY = 0


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
        self.capacity = 5   # maximum storage capacity 
        self.battery = 100    #placeholder for the battery threadhold
        self.type = "picker_robot"
        
        
        
    @property
    def Reach(self) -> list:
        #make list of positions to return
        #take current position
        # for ever quare that this can reach
        # add the offset position to the list
        positions = []
        c_x, c_y = self.pos
        for x in range(-3, 4):
            for y in range (-3, 4):
                if x < 0:
                    continue
                if x > self.model.grid.width:
                    continue
                if y < 0 :
                    continue
                if y > self.model.grid.height:
                    continue
                
                
                
                positions.append((c_x + x, c_y + y))
                
        return positions
            
            
    
    
    @property 
    def is_busy(self):
        return self.state == BUSY
    
    
    def step(self):
        """ 
        Define teh behaviour of the robot at each step 
        """
        print(f"PickerRobot {self.unique_id} is taking a step at position {self.pos}.")         #debug
        action = self.make_decision()
        print(f"PickerRobot {self.unique_id} decided to : {action }")     #debug print for the visual movement of pickerrobot 
        getattr(self,action)()
        
        
        
    # def make_decision(self):
    #     """ 
    #     Decide the next action based on the robot's state and surroundings 
    #     """
    #     print(f"PickerRobot {self.unique_id} is making a decision.")      # debugging
    #     from model import CropAgent     #imported locally 
    #     if self.state == FREE:  
    #         #check if the robot is near the crop ( cropAgent)
    #         crop_nearby = any (isinstance(a, CropAgent) for a in self.model.grid.get_neighbors(self.pos, moore = True))
    #         print(f"Crop Nearby: {crop_nearby}")      #debugging
    #         return "pick" if crop_nearby else "move_randomly"
    #     elif self.state == BUSY:
    #         #return to the base when it is rull
    #         return "return_to_base" if self.storage >= self.capacity else "move_randomly"
    #     else:
    #         return "wait"   #Default action     # could it be keep moving or ?
        
        
        
    # def move_randomly(self):    # responbile for movign the robot 
    #     """ 
    #     Move the robot to a random neighboring cell, avoiding trees 
    #     """
    #     from model import TreeAgent    # imported locally only before they are called / if imported globally at the top, it is circulr dependency with model.py
    #     possible_steps = self.model.grid.get_neighborhood(
    #         self.pos, moore = True, include_center=False
    #     )
    #     valid_steps = [step for step in possible_steps if not any(isinstance (a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))]
    #     print(f"PickerRobot {self.unique_id} valid steps: {valid_steps}")    # debugging 
    #     if valid_steps:
    #         new_position = self.random.choie(valid_steps)
    #         self.model.grid.move_agent(self, new_position)
    #         print(f"PickerRobot {self.unique_id} moved to {new_position}")     #debug 
            
            
            
    
    #temporary function to test random movement of the robots without constrainst , no restrictions to water and  trees.
    def move_randomly(self):
        """
        Move the robot to a random neighboring cell, without any restrictions.
        """
        possible_steps = self.modle.grid.get_neighborhood(
            self.pos, moore = True, include_center = False 
        )
        if possible_steps:
            new_position = self.random.choice(possible_steps)
            self.modle.grid.move_agent(self, new_position)
            print(f"PickerRobot {self.unique_id} moved to {new_position}")     #debug 
            
            
            
            
            
            
            
    def pick(self):
        """ 
        Pick the strawberry if one is in the current cell
        """
        from model import CropAgent     #imported locally 
        
        # get the reach
        # for each in reach 
        
        reachable = self.Reach
        
        print(reachable)
        
        crops = [ a for a in self.model.grid.get_cell_list_contents(self.pos)if isinstance (a, CropAgent)]
        if crops:
            crop = crops[0]
            self.model.grid.remove_agent(crop)
            self.storage += 1
            print(f"Picked a strawberry at {self.pos} . Storage: {self.storage}")
            
    
    
    def return_to_base(self):
        """ 
        Move toward to the base to drop off crops       ( battery charging to be added later )
        """
        base_x, base_y = 0,0  
        current_x, current_y = self.pos
        dx = base_x - current_x      ##????
        dy = base_y - current_y 
        move_x = current_x +  ( 1 if dx > 0 else -1 if dx < 0 else 0 )
        move_y = current_y +  (1 if dy > 0 else -1 if dy < 0 else 0 )
        new_position = (move_x, move_y)
        if self.model.grid.is_cell_empty(new_position):
            self.model.grid.move_agent(self, new_position)
            
            
            
    def wait(self):
        """
        wait in place when its not full capacity or nothing to do 
        """
        pass
    
    
    
        
                  
                  
                  
        
        
    


































# import mesa 



# NUMBER_OF_CELLS = 50 
# BUSY = 0 
# FREE = 1 
# UNDONE = 0 
# DONE = 1 


# #defining the class for robots 
# class PickerRobot(mesa.Agent):
#     """Represents a strawberry picker robot in the farm """ 
#     def __init__ ( self, id, pos, model , init_state = FREE):
#         """Initialise state attributes, including: 
#         * current and next position of the robot 
#         * state (FREE/ BUSY)
#         * payload (id of any box the robot is carrying )
#         """
#         super().__init__(id, model)
#         self.x, self.y = pos
#         self.next_x, self.next_y = None, None 
#         self.state = init_state 
#         self.payload = None 
        
        
        
#     @property 
#     def isBusy (self):
#         return self.state == BUSY
    
    
    
#     def step (self):
#         """
#         *Obtain action as a result of deliberation 
#         * trigger action 
#         """
#         action = getattr(self,self.make_decision())
#         action ()
        
        
        
#         #Robot decision model 
        
        
#     def make_decision (self):
#         """
#         Simple Rule-Based  architecture , should determine the action to execute based on the robot state. 
#         """
#         action = "wait"
#         if self.state == FREE:
#             next_position = (self.x + 1 , self.y )
#             if not self.model.is_cell_empty (next_position):
#                 action  = "pick"
#             elif next_position [0] < NUMBER_OF_CELLS -1 :
#                 action = "move_fw"
                
#         else: 
#             if self.pos[0]-1 == 0:
#                 action = "drop_off"
#             else:
#                 action = "move_bw"
#         return action
    
    
    
#      # Robot Actions
     
#     def move(self):
#         """ 
#         Move robot to the next position 
#         """
        
#         self.model.grid.move_agent(self,(self.next_x, self.next_y))
        
        
    
#     def move_payload(self):
#         """
#         *Obtains the box whose id is in the payload (Hint you can use the method: self.model.schedule.agents to iterate over existing agents)
#         *Move teh payload together with the robot
#         """
#         box = [ a for a in self.model.schedule.agents if isinstance(a,crops) and a.unique_id == self.payload ] 
        
        
#         if len(box)>0:
#             self.model.grid.move_agent(box[0], (self.x, self.y))
            
            
#     def wait(self):
#         """
#         Keep the same position as the current one 
#         """
#         self.next_x = self.x
#         self.next_y = self.y
        
        
    
#     def move_fw(self):
#         """
#         Move the robot towards the boxes from left to right
        
#         """
        
#         self.next_x = self.x + 1
#         self.next_y = self.y
#         self.move()
        
        
#     def move_bw(self):
#         """
#         Move the robot and teh payload towards the collection point (right to left)
#         """
        
#         self.next_x = self.x - 1
#         self.next_y = self.y 
#         self.move()
#         self.move_payload()
        
        
        
#     def pick(self):
#         """ 
#         * change robot state to busy 
#         * find out the id of the box next to the robot
#         * store the box id in the payload of the robot
#         """
        
#         self.state = BUSY
#         nbs = [nb for nb in self.model.grid.get_neighbors((self.x,self.y),False)]
        
        
#         for i in range(len(nbs)):
#             if isinstance(nbs[i],crops):
#                 box = nbs[0]
    