import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)
from mesa import Model, Agent
from mesa.space import MultiGrid
from mesa.time import BaseScheduler
from agents import PickerRobot
from agents import DroneRobot



#############################################################
           ### Farm Model Class Initialisation
#############################################################


class FarmModel(Model):
    def __init__(self, width= 25, height=25, num_robots = 2):
        """
        Initialize the farm model with the given width and height.
        """
        super().__init__()  # Explicitly initialize the Model class
        print("Initialising FarmModel......")   #debug
        self.grid = MultiGrid(width, height, torus=False)  # Non-toroidal grid
        self.schedule = BaseScheduler(self)  # Scheduler for agents



#############################################################
           ### Terrain Coordinates Definition 
#############################################################



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
        


#############################################################
           ### Calling terrain functions
#############################################################


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
        
    

#############################################################
           ### ROBOTS initialisation
#############################################################

        # # ADDING DRONES , 
        # for i in range ( num_robots):
        #     print(f"Attempting to place DroneRobot {i}...")    #debug
        #     from agents import DroneRobot   
        #     x = self.random.randint(0, self.grid.width -1)
        #     y = self.random.randint(0, self.grid.height -1)
        #     while not self.grid.is_cell_empty((x,y)):
        #         x = self.random.randint(0, self.grid.width -1)
        #         y = self.random.randint(0, self.grid.height -1)
        #     print(f"Placing DroneRobot {i} at {(x, y)}")  # Debug print
        #     drone_robot = DroneRobot( self.next_id(), (x,y), self)
        #     print(f"Placing DroneRobot at {x}, {y}")
        #     self.grid.place_agent(drone_robot, (x,y))
        #     self.schedule.add(drone_robot)
            


            
        ### debug drone init ##
        for i in range(num_robots):
            print(f"Attempting to place DroneRobot {i}...")
            x = self.random.randint(0, self.grid.width - 1)
            y = self.random.randint(0, self.grid.height - 1)
            drone_robot = DroneRobot(self.next_id(), (x, y), self)
            self.grid.place_agent(drone_robot, (x, y))
            self.schedule.add(drone_robot)
            print(f"DroneRobot {i} placed at {(x, y)}.")




        ## ADDING PICKER ROBOT , INITIALISATION     #difference to last one working with battery 
        ####robot placement anywhere apart from water and tree grids   ## works works works this one works 
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


        

        
            

#############################################################
           ##Functions for Terrains
#############################################################
    
    #New 
    def create_water(self, water_coordinates):
        for (x,y) in water_coordinates:
            #print (f"Placing WaterAgent at ({x}, {y})")
            water_agent = WaterAgent(self.next_id() ,(x,y), self)
            self.grid.place_agent(water_agent, (x,y))
            self.schedule.add(water_agent)
                    


    def create_trees(self, tree_coordinates):
        for start_point, end_point in tree_coordinates:
            start_x, start_y = start_point
            end_x, end_y = end_point
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    #print(f"Placing TreeAgent at ({x}, {y})")
                    tree_agent = TreeAgent(self.next_id() ,(x, y), self)
                    self.grid.place_agent(tree_agent, (x, y))
                    self.schedule.add(tree_agent)
    
    
    
    
    ##crops functions meant for overlapping on trees
    def create_crops(self, crops_coordinates):
        for (x, y) in crops_coordinates:
            #Check if the cell contains a TreeAgent
            existing_agents = self.grid.get_cell_list_contents((x,y))
            has_tree = any(isinstance(agent, TreeAgent)for agent in existing_agents)
            
            
            if not has_tree:
                #print(f"Skipping CropAgent at ({x},{y})")
                continue      #skip this position if there is no tree
            
            
            #place the CropAgent
            #print(f"Placing CropAgent at ({x}, {y})")
            crop_agent = CropAgent(self.next_id(), (x,y), self)
            self.grid.place_agent(crop_agent, (x,y))
            self.schedule.add(crop_agent)
            
            
    
    #New function for path coordinates defined in a list path_coordinates  , and called  in function self.create_path(path_coordinates)      
    def create_path(self, path_coordinates):
        for (x,y) in path_coordinates:
            #print(f"Placing PathAgent at ({x}, {y})")
            path_agent = PathAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(path_agent, (x, y))
            self.schedule.add(path_agent)
            
    
    #New function for base with 4 coordinates ,
    def create_base(self, base_coordinates):
        for (x, y) in base_coordinates:
            #print(f"Placing BaseAgent at ({x}, {y})")
            base_agent = BaseAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(base_agent, (x, y))
            self.schedule.add(base_agent)
            self.pos = (x,y)
            
    
    # def step(self):
    #     print("Advancing the model by one steppppppppp ")
    #     self.log_cell_contents()      #inspect the grid contents at each step ( debug )
    #     self.schedule.step()
    
    def step(self):
        self.schedule.step()




#############################################################
           ### Classes for terrains 
#############################################################


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
        
        
        
# class PickerRobot(Agent):
#     def __init__(self, unique_id, pos, model):
#         super().__init__(unique_id, model)
#         self.type= "picker_robot"
#         self.pos = pos




#############################################################
           ### MODEL SIMULATION
#############################################################

        
# important !!! to get the model started 
def step(self):
       """ 
       Advance the model by one step. 
       """
       print("Advancing the model by one step.")    #debugging 
       self.schedule.step()     #triggers all agents step methods 
    


### Debug GUI Test ######

model = FarmModel(width=25, height=25, num_robots=2)
for i in range(10):
    print(f"Step {i}")
    model.step()
