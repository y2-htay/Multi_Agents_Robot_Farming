import mesa
from mesa import Agent
#from .model import FREE, BUSY
#from model import TreeAgent, CropAgent

BATTERY_SKIP_THRESHOLD = 5

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
        self.battery_tick = 0
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
                if c_x + x < 0:
                    continue
                if c_x + x > self.model.grid.width:
                    continue
                if c_y + y < 0 :
                    continue
                if c_y + y > self.model.grid.height:
                    continue
                
                
                
                positions.append((c_x + x, c_y + y))
                
        return positions
        
    
    
    # @property 
    # def is_busy(self):
    #     return self.state == BUSY
    
    
    def step(self):
        """ 
        Define teh behaviour of the robot at each step 
        """
        print(f"PickerRobot {self.unique_id} is steppign at position {self.pos}.")
        print("battery for ", self.unique_id, " = ", self.battery)
        
        self.battery_tick += 1
        
        if self.battery_tick == BATTERY_SKIP_THRESHOLD:
            self.battery_tick = 0
            self.battery -= 1
            
        
        print(f"PickerRobot {self.unique_id} is taking a step at position {self.pos}.") #debug
        #Decision making 
        action = self.make_decision()
        print(f"PickerRobot {self.unique_id} decided to : {action }")     #debug print for the visual movement of pickerrobot 
        getattr(self,action)()        #execuse the chosen action 
        
        
    # def advance(self) -> None:
        
       
            
    #     # if self.battery < 1:
    #     #     return
    
    
    
    ###########
    
    def make_decision(self):
        """ 
        Decide the next action based on the robot's state and surrondings.
        """
        print(f"PickerRobot {self.unique_id} is making a decision.")
        from farm_model import CropAgent     
        
        if self.battery <= 0 :
            return "return_to_base"
        
        if self.state == FREE:
            #Check if there is a cropagent nearby (ignore treeagent )
            crop_nearby = any(
                isinstance(agent, CropAgent)
                for agent in self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 3)
            )
            print(f"PickerRobot {self.unique_id} Crop Nearby: {crop_nearby}")
            return "pick" if crop_nearby else "move_randomly"
        elif self.state == BUSY:
            return "return_to_base" if self.storage >= self.capacity else "move_randomly"
        
        return "wait"
        
   ###################function after battery ############
        
    # def make_decision(self):
    #     """ 
    #     Decide the next action based on the robot's state and surroundings 
    #     """
    #     print(f"PickerRobot {self.unique_id} is making a decision.")      # debugging
    #     from model import CropAgent     #imported locally 
        
    #     if self.battery < 0:
    #         return "wait"
        
    #     if self.state == FREE:  
    #         #check if the robot is near the crop ( cropAgent)
    #         ##crop_nearby = any (isinstance(a, CropAgent) for a in self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 3))    ####TODO:change this useless lineeeeeee 
    #         crop_nearby = any(isinstance(a, CropAgent) for a in self.model.grid.get_neighbors(self.pos, moore=True, include_center = False, radius =3))
    #         ## get the if statement  from pick  - check if that is a crop
    #         print(f"PickerRobot {self.unique_id} Crop Nearby: {crop_nearby}")      #debugging
    #         return "pick" if crop_nearby else "move_randomly"
    #     elif self.state == BUSY:
    #         #return to the base when it is rull
    #         return "return_to_base" if self.storage >= self.capacity else "move_randomly"
    #     else:
    #         return "wait"   #Default action     # could it be keep moving or ?
        
    ######################################################
    
    ##########function before battery ################
    
    
        
    def move_randomly(self):    # responbile for movign the robot 
        """ 
        Move the robot to a random neighboring cell, avoiding trees 
        """
        from farm_model import TreeAgent
        #from model import CropAgent
        # imported locally only before they are called / if imported globally at the top, it is circulr dependency with model.py
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
            self.model.grid.move_agent(self, new_position)
            print(f"PickerRobot {self.unique_id} moved to {new_position}")     #debug 
            
            
    
    # #temporary function to test random movement of the robots without constrainst , no restrictions to water and  trees.
    # def move_randomly(self):
    #     """
    #     Move the robot to a random neighboring cell, without any restrictions.
    #     """
    #     possible_steps = self.model.grid.get_neighborhood(
    #         self.pos, moore = True, include_center = False 
    #     )
    #     if possible_steps:
    #         new_position = self.random.choice(possible_steps)
    #         self.model.grid.move_agent(self, new_position)
    #         print(f"PickerRobot {self.unique_id} moved to {new_position}")     #debug 
            
            
            
            
    def pick(self):
        """ 
        Pick the strawberry if one is in the current cell
        """
        print(f"Hey I am ready to pickkkkkkkkkk the strawberry ")
        from farm_model import CropAgent     #imported locally 
        
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
                
            
            # crops = [ a for a in self.model.grid.get_cell_list_contents(each)if isinstance (a, CropAgent)]
            # if crops:
            #     crop = crops[0]
            #     self.model.grid.remove_agent(crop)
            #     self.storage += 1
            #     print(f"Picked a strawberry at {each} . Storage: {self.storage}")
            
            
    
    
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
    
    
    # Djoikstra's algorithm
    
    #station name--> tuples()
    
    #covert the tuples into strings
    
    #store the hash in place of the station
    
    #when making the hash, also save the
    
    
    
    #expand the reach ,, neighbors 
    
    #add the stages of fruits - tree, green , yellow, ripe 
    

