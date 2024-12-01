
from mesa import Model, Agent
from mesa.space import MultiGrid
from mesa.time import BaseScheduler
from agents import PickerRobot



class FarmModel(Model):
    def __init__(self, width= 25, height=25, num_robots = 2):
        """
        Initialize the farm model with the given width and height.
        """
        super().__init__()  # Explicitly initialize the Model class
        self.grid = MultiGrid(width, height, torus=False)  # Non-toroidal grid
        self.schedule = BaseScheduler(self)  # Scheduler for agents

        
        #Terrain Setup
        tree_ranges = [
    ((0, 2), (0,24)),
    ((1,2), (1,24)),
    ((4,0), (4,22)),
    ((5,0), (5,22)),
    ((8,2), (8,24)),
    ((9,2), (9,24)),
    ((16,2), (16,24)),
    ((17,2), (17,24)),
    ((20,0), (20,22)),
    ((21,0), (21,22)),
    ((24,2), (24,24))
]
        
        
        #New Water Coordinates
        water_ranges = [(x, y) for x in [12, 13] for y in range(23)]
        
        
        #New Crops Coordinates 
        crops_coordinates = [
    (0, 4), (0, 5), (0, 12), (0, 13), (0, 20), (0, 23),
    (1, 7), (1, 8), (1, 9),
    (4, 5), (4, 6), (4, 15), (4, 16), (4, 21),
    (8, 8), (8, 11), (8, 18), (8, 19), (8, 20),
    (9, 3), (9, 4), (9, 15),
    (16, 5), (16, 6), (16, 9), (16, 14), (16, 15), (16, 19), (16, 20), (16, 23),
    (17, 2), (17, 9), (17, 12), (17, 19), (17, 20), (17, 23),
    (20, 3), (20, 4), (20, 13), (20, 21),
    (21, 0), (21, 7), (21, 10), (21, 13), (21, 18), (21, 19),
    (24, 5), (24, 6), (24, 11), (24, 12), (24, 16), (24, 21), (24, 22)
]
                
        
        #New base now with four coordinates /four cell grids 
        base_coordinates = [
    (0, 0), (0, 1), (1, 0), (1, 1)
]
        
        
        #Generating the coordinates in a loop rather than defining all these 
        path_coordinates =[]
        
        # Example: Generate paths along specific columns or rows
        for x in [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23]:
            for y in range(25):  # Assuming 0-24 rows
                path_coordinates.append((x, y))

        # Adding specific points like (4, 23), (12, 23), etc.
        path_coordinates.extend([(4, 23), (4, 24) , (5,23), (5,24), (8,0), (8,1), (9,0),(9,1), (12, 23), (12, 24),(13,23),(13,24),(16,0),(16,1),(17,0),(17,1),(20,23),(20,24),(21,23),(21,24),(24,0),(24,1)])
        



        # Add terrain agents
       # self.create_water(start_point=(6,0), end_point=(6,24))
        self.create_water(water_ranges)      #for new water coordinates loop 
        self.create_trees(tree_ranges)
    # #    # self.create_crops([
    # #         (4,13), (4,14), (2, 8), (3, 8), (4, 8), (10,16), (10,17), 
    # #     ])       # for old coordinates 
        self.create_crops(crops_coordinates)     #for new coordinates   # created a list of coordinates separate instead of calling in the function 
    # #    self.create_path(start_point=(1, 0), end_point=(1, 24))    #old path coordinates
        self.create_path(path_coordinates)      #for new path coordinates;
        self.create_base(base_coordinates)
        
        
        
        ### Debug : log the grid contents after initialisation
        self.log_cell_contents()
        
        
        #old function that worked for old grid ( not shoiwng anything )
        # for i in range(num_robots):
        #     x = self.random.randint(0, width -1)
        #     y = self.random.randint(0, height -1)
        #     while not self.grid.is_cell_empty((x,y)):
        #         x = self.random.randint(0, width -1)
        #         y = self.random.randint(0, height -1)
        #     print(f"Creating Picker Robot with id = {self.next_id()}, pos = {(x,y)}, model = {self}")
        #     picker_robot = PickerRobot(self.next_id(),(x,y),self)
        #     self.grid.place_agent(picker_robot,(x,y))
        #     self.schedule.add(picker_robot)
        
        


        # print("Starting to place PickerRobot agents.....")
        # for i in range (num_robots):
        #     print(f"Attempting to place PickerRobot {i} ....)")
        #     max_attempts = 100
        #     attempts = 0
        #     while attempts < max_attempts:
        #         x = self.random.randint(0, self.grid.width -1)
        #         y = self.random.randint(0, self.grid.height -1)
        #         if self.grid.is_cell_empty((x,y)):
        #             print(f"Placing Picker Robot {i} at position {(x,y)} ")
        #             picker_robot = PickerRobot(self.next_id(), (x,y), self)
        #             self.grid.place_agent(picker_robot, (x,y))
        #             self.schedule.add(picker_robot)
        #             break
        #         attempts +=1
        #         print(f"Finished placing PickerRobot agents.")
        #     else:
        #         print(f"Failed to place Picker Robot{i} after {max_attempts} attempts.")
        
        

        #debug for testing placement for pickerrobots ( placing only one robot)
        # for i in range(num_robots):
        #     x = self.random.randint(0, width -1)
        #     y = self.random.randint(0, height - 1)
        #     while not self.grid.is_cell_empty((x,y)):
        #         x = self.random.randint(0, width - 1)
        #         y = self.random.randint(0, height -1)
        #         print("Starting PickerRobot Placement")
        #         picker_robot = PickerRobot (self.next_id(), (0,0), self)
        #         self.grid.place_agent(picker_robot, (0,0))
        #         self.schedule.add(picker_robot)


        # testing robot placement anywhere apart from water and tree grids   ## works works works this one works 
        for i in range(num_robots):
            while True:
                x = self.random.randint(0, self.grid.width - 1)
                y = self.random.randint(0, self.grid.height - 1)

                # Get contents of the cell
                contents = self.grid.get_cell_list_contents((x, y))

                # Check conditions
                has_tree_or_water = any(isinstance(agent, (TreeAgent, WaterAgent)) for agent in contents)
                is_valid_cell = any(isinstance(agent, (PathAgent, BaseAgent)) for agent in contents)

                if not has_tree_or_water and is_valid_cell:
                  print(f"Placing PickerRobot at ({x}, {y})")  # Debug
                  picker_robot = PickerRobot(self.next_id(), (x, y), self)
                  self.grid.place_agent(picker_robot, (x, y))
                  self.schedule.add(picker_robot)
                  break  # Exit loop after successfully placing
                else:
                  print(f"Invalid cell for PickerRobot at ({x}, {y}), retrying...")  # Debug



        
    ##debug 
    def log_cell_contents(self):
        """ Log the contents of each cell in the grid."""
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                contents = self.grid.get_cell_list_contents((x,y))
                if contents:
                    print(f"Cell ({x},{y}) contains: {[type(agent).__name__ for agent in contents]}")
                if any(isinstance(agent, PickerRobot) for agent in contents):
                    print(f"PickerRobot located at ({x}, {y})")
                    
                    
    ##debug                
    # def place_agent_safe(self, agent, position):
    #     # Check if the agent is already at the position
    #     if self.grid.is_agent_at(position):  # Assuming you have a method to check this
    #         current_agent = self.grid.get_agent_at(position)  # Get the current agent at the position
    #         self.grid.remove_agent(current_agent)  # Remove the agent from its current position
    #     self.grid.place_agent(agent, position)  # Now place the new agent safely    
        
        
        
        
        
        
        
        
        # # #add picker robot  ( locate for the initial grid ) 
        # for i in range (num_robots):
        #     while True:     #continue until a valid position is found 
        #         x = self.random.randint(0, self.grid.width -1)
        #         y = self.random.randint(0, self.grid.height - 1) 
                
        #         #Debug : check and log cell contents 
        #         contents = self.grid.get_cell_list_contents((x,y))
        #         print(f"Position {(x,y)} contentes: {contents}")
                
                
                
        #         #check if the cell is empty and valid 
        #         if not self.grid.is_cell_empty((x,y)):
        #             print(f"Position{(x,y)} is not empty, finding a new position.")
        #             continue     #skip to the next iteration to find an empty position
                
                
                
                
        #         #check if the cell contains any tree or crop agents
        #         if any (isinstance(agent, TreeAgent) for agent in self.grid.get_cell_list_contents((x,y))):
        #             print(f"Position {(x,y)} contains a tree agent, finding a new position.")
        #             continue   #skip to the next iteration 
        #             #valid position foound; place the pickerrobot
        #             #continue       #skip this cell and find a new one
        #         #if no tree or crop agents, place the PickerRobot
                
        #         #if the position is  valid, place the pickerrobot
        #         print(f"Creating PickerRobot with id = {self.next_id()},pos ={(x,y)}, model = {self}")
        #         picker_robot = PickerRobot(self.next_id(),(x,y),self)
        #         self.grid.place_agent(picker_robot,(x,y))
        #         self.schedule.add(picker_robot)
        #         print(f"PickerRobot {picker_robot.unique_id} added to the schedule.")     #debugging for picker added to the schedule 
        #         break       #exit the while loop after placing the robot 
            
            
            
            
        # for i in range(num_robots):
        #     while True:       
        #         x = self.random.randint(0,self.grid.width - 1) 
        #         y = self.random.randint(0, self.grid.height -1)
                
                
                
        #         if self.grid.is_cell_empty((x,y)):
        #             print(f"Placing PickerRobot at {self.next()} at {(x,y)}.")
        #             picker_robot = PickerRobot(self.next_id(), (x,y), self)
        #             self.grid.place_agent(picker_robot, (x,y))
        #             self.schedule.add(picker_robot)
            
            
            
            
            #While true
            
                #for each agent in the coordinate (x,y)
                
                    #if agent is a tree
                    #continue
                    
                    #if the agent is a crop
                        #continue
                    
                    #place robot
                
                
            
            
            # while not self.grid.is_cell_empty((x,y)):
            #     x = self.random.randint(0, width -1)
            #     y = self.random.randint(0, height - 1)
            # print(f"Creating PickerRobot with id = {self.next_id()}, pos = {(x,y)}, model={self}")     #debug print for arguments passed to pickerrobot in the farmmodel constructor
            # picker_robot = PickerRobot (self.next_id(), (x,y), self)
            # self.grid.place_agent(picker_robot, (x,y))
            # self.schedule.add(picker_robot)
            

#############################################################
           ##Functions for Terrains
#############################################################

                
    #old function for creating from the loop self.create_water(start_point=(6,0), end_point=(6,24))
    # def create_water(self, start_point, end_point):
    #     start_x, start_y = start_point
    #     end_x, end_y = end_point
    #     for x in range(start_x, end_x + 1):
    #         for y in range(start_y, end_y + 1):
    #             print(f"Placing WaterAgent at ({x}, {y})")
    #             water_agent = WaterAgent((x, y), self)
    #             self.grid.place_agent(water_agent, (x, y))
    #             self.schedule.add(water_agent)
                
    
    #new function for creating water for new coordinates (in a loop range)
    # def create_water(self, water_coordinates):
    #     for start_point, end_point in water_coordinates:
    #         start_x, start_y = start_point
    #         end_x, end_y = end_point 
    #         for x in range(start_x, end_x +1):
    #             for y in range(start_y, end_y +1):
    #                 print (f"Placing WaterAgent at ({x}, {y})")
    #                 water_agent = WaterAgent((x,y), self)
    #                 self.grid.place_agent(water_agent, (x,y))
    #                 self.schedule.add(water_agent)
                    
                    
    
    #New 
    def create_water(self, water_coordinates):
        for (x,y) in water_coordinates:
            print (f"Placing WaterAgent at ({x}, {y})")
            water_agent = WaterAgent(self.next_id() ,(x,y), self)
            self.grid.place_agent(water_agent, (x,y))
            self.schedule.add(water_agent)
                    


    def create_trees(self, tree_coordinates):
        for start_point, end_point in tree_coordinates:
            start_x, start_y = start_point
            end_x, end_y = end_point
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    print(f"Placing TreeAgent at ({x}, {y})")
                    tree_agent = TreeAgent(self.next_id() ,(x, y), self)
                    self.grid.place_agent(tree_agent, (x, y))
                    self.schedule.add(tree_agent)
    
    
    # def create_trees(self, tree_coordinates):
    #     for (x,y) in tree_coordinates:
    #         print(f"Placing TreeAgent at ({x}, {y})")
    #         tree_agent = TreeAgent(self.next_id() ,(x, y), self)
    #         self.grid.place_agent(tree_agent, (x, y))
    #         self.schedule.add(tree_agent)
            
            
    
    ## same function for crops defined in a list , 
    # def create_crops(self, crops_coordinates):
    #     for (x, y) in crops_coordinates:
    #         print(f"Placing CropAgent at ({x}, {y})")
    #         crop_agent = CropAgent(self.next_id() ,(x, y), self)
    #         #crop_agent = CropAgent(self.next_id,(x,y), self)
    #         self.grid.place_agent(crop_agent, (x, y))
    #         self.schedule.add(crop_agent)
    
    
    
    ##crops functions meant for overlapping on trees
    def create_crops(self, crops_coordinates):
        for (x, y) in crops_coordinates:
            #Check if the cell contains a TreeAgent
            existing_agents = self.grid.get_cell_list_contents((x,y))
            has_tree = any(isinstance(agent, TreeAgent)for agent in existing_agents)
            
            
            if not has_tree:
                print(f"Skipping CropAgent at ({x},{y})")
                continue      #skip this position if there is no tree
            
            
            #place the CropAgent
            print(f"Placing CropAgent at ({x}, {y})")
            crop_agent = CropAgent(self.next_id(), (x,y), self)
            self.grid.place_agent(crop_agent, (x,y))
            self.schedule.add(crop_agent)
            
            
    #old function for coordinates in a looop  self.create_path(start_point=(1, 0), end_point=(1, 24)) 
    # def create_path(self, start_point, end_point):
    #     start_x, start_y = start_point
    #     end_x, end_y = end_point
    #     for x in range(start_x, end_x + 1):
    #         for y in range(start_y, end_y + 1):
    #             print(f"Placing PathAgent at ({x}, {y})")
    #             path_agent = PathAgent((x, y), self)
    #             self.grid.place_agent(path_agent, (x, y))
    #             self.schedule.add(path_agent)
                
    
    #New function for path coordinates defined in a list path_coordinates  , and called  in function self.create_path(path_coordinates)      
    def create_path(self, path_coordinates):
        for (x,y) in path_coordinates:
            print(f"Placing PathAgent at ({x}, {y})")
            path_agent = PathAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(path_agent, (x, y))
            self.schedule.add(path_agent)
            
            
                
                
    
    
    # #old function for when base is only one grid at the corner    
    # def create_base(self):
    #     """
    #     Add base station to the grid along the column = 0 
    #     """
    #     base_position = (0, 0) 
    #     print(f"Base position: {base_position}")
    #     base_agent = BaseAgent(base_position, self)
    #     self.grid.place_agent(base_agent, base_position)
    #     self.schedule.add(base_agent)
        
    def step(self):
        self.schedule.step()
    

    
    #New function for base with 4 coordinates ,
    def create_base(self, base_coordinates):
        for (x, y) in base_coordinates:
            print(f"Placing BaseAgent at ({x}, {y})")
            base_agent = BaseAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(base_agent, (x, y))
            self.schedule.add(base_agent)
            self.pos = (x,y)
            
    
    def step(self):
        self.log_cell_contents()      #inspect the grid contents at each step ( debug )
        self.schedule.step()
            

class WaterAgent(Agent):   #an agent representing a tree on the grid 
    def __init__(self, _id, pos, model):
        super().__init__( _id, model)
        self.type = "water"
        self.pos = pos


class TreeAgent(Agent):
    def __init__(self, _id ,pos,  model):
        super().__init__(_id, model)
        self.type = "tree"
        self.pos = pos


class CropAgent(Agent):
    def __init__(self,  _id, pos, model):
        super().__init__( _id,  model)
        self.type = "crop"
        self.pos = pos
        #super().__init__(_id, model)


class PathAgent(Agent):
    def __init__(self, _id, pos, model):
        super().__init__( _id, model)
        self.type = "path"
        self. pos = pos 
        

class BaseAgent(Agent):
    def __init__(self,  _id, pos, model):
        super(). __init__( _id, model)
        self.type = "base"
        self.pos = pos
        
        
        
class PickerRobot(Agent):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.type= "picker_robot"
        self.pos = pos
        
        
## important !!! to get the model started 
def step(self):
    """ 
    Advance the model by one step. 
    """
    print("Advancing the model by one step.")    #debugging 
    self.schedule.step()     #triggers all agents step methods 
    