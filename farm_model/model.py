# import mesa
# from mesa import Model, Agent
# from mesa.space import MultiGrid
# from mesa.time import BaseScheduler 


# class FarmModel(Model):
#     def __init__(self, width, height):
#         #Initialize the parent Model class
#         super().__init__()
        
#         #set model parameters
#         self.width  = width 
#         self.height = height 
        
#         #create the grid and scheduler
#         self.grid = MultiGrid(width, height, torus=False)   # torus for wrapping around the edges
#         self.schedule = BaseScheduler(self)
#         self.index_counter = 0  #initize  unique ID counter
        
        
#        #create the environment 
#         self.create_water()
#         self.create_crops()
#         self.create_paths()
#         self.create_trees()
       
       
#     #generate the next unique ID number 
#     def next_id(self):
#         return self.index_counter
    
    
#     #increment the unique ID counter
#     def increment_id(self):
#         self.index_counter += 1
    
    
    
       
       
       
#     # def create_water(self):
#     #     #create water cells in the grid
#     #     for x in range(1, self.width, 3):  #place water at every 3 cells
#     #      for y in range(1, self.height, 3):   
#     #          self.grid.place_agent(Terrain("TREE"), (x,y))
    
    
#     def add_water(self, water_coordinates, is_deep=False):
#       for (y, x) in water_coordinates:
#           water_cell = Water(self.next_id, (x,y), self, is_deep )
#           print(f"Creating water at ({x}, {y}) with ID {water_cell.unique_id}"
#                 f" and depth {'deep'if is_deep else 'shallow'}.")
#           self.grid.place_agent(water_cell, (x,y))
#           self.increment_id()
                
            
            
#     water_coordinates = [(i,6) for i in range(25)]   #water vertical column at x=6
#         self.add_water(water_coordinates, is_deep=True)
        
        
         
        
                
             
             
#     def create_crops(self):
#         ripe_positions = [(3,4),(9,6),(15,2)]
#         for x in range(0,self.width,4):
#             for y in range(0, self.height, 4):
#                 f
              
        




# from mesa import Model, Agent
# from mesa.space import MultiGrid
# from mesa.time import BaseScheduler

# class FarmModel(Model):
#     def __init__(self, width = 11, height = 25):
#         """
#         Initialize the farm model with the given width and height.
#         """
#         super().__init__()     #### 
#         # Mesa components: grid and scheduler
#         self.grid = MultiGrid(width, height, torus=False)  # Create a non-toroidal grid
#         self.schedule = BaseScheduler(self)  # Set up the scheduler
        

#         # Add terrain agents
#         # self.create_water()
#         # self.create_trees()
#         # self.create_crops()
#         # self.create_path()

    
#         tree_ranges = [
#             ((0, 0), (22, 0)),     # first range - column 0 from row 0 to 22     #row,column format 
#             ((3, 2), (24, 2)),     # second range - column 2 from row 3 to 24
#             ((0, 4), (13, 4)),     # 
#             ((15, 4), (21, 4)),
#             ((6, 8), (23, 8)),
#             ((0, 9), (10, 9))
             
#         ]

#         crops_coordinates = [(0, 0), (13, 4), (14, 4), (2, 8), (3, 8), (4, 8), (16, 10), (17, 10)]



#         #add terrain agents 
#         self.create_water(start_point=(0,6), end_point =(24,6))
#         self.create_trees(tree_ranges)
#         self.crate_crops(crops_coordinates)
#         self.create_path(start_point=(1,0), end_point= (1,24))
        
        
        
#         # Grid configuration
#     # grid_width = 11
#     # grid_height = 25


#     # def create_water(self):
#     #     """
#     #     Add water agents to the grid at predefined coordinates.
#     #     """
#     #     water_coordinates = [(i, 6) for i in range(25)]  # Vertical river at column 6

#     #     for (x, y) in water_coordinates:
#     #         # Create and place a WaterAgent
#     #         water_agent = WaterAgent((x, y), self)
#     #         self.grid.place_agent(water_agent, (x, y))
#     #         self.schedule.add(water_agent)
    
    
#     def create_water(self, start_point, end_point):
#         """Add water to the grid with specified range"""
#         start_x , start_y = start_point
#         end_x, end_y = end_point
        
        
#         for x in range (start_x, end_x + 1):     #+ 1 to include the end_x ( start with index 0 )
#             for y in range (start_y, end_y + 1 ):    # +1 to include the end_y (index 0 starting point ) 
#                 water_agent = WaterAgent ((x,y), self) 
#                 self.grid.place_agent(water_agent, (x,y))
#                 self.schedule.add(water_agent)        
                
                
#         # self.create_water(start_point=(0,6), end_point =(24,6))
                
                    

#     # def create_trees(self):
#     #     """
#     #     Add tree agents to the grid at predefined coordinates.
#     #     """
#     #     tree_coordinates = [(i, 0) for i in range(23)] + \
#     #                        [(i, 2) for i in range(3, 25)] + \
#     #                        [(i, 4) for i in range(14)] + \
#     #                        [(i, 4) for i in range(15, 22)] + \
#     #                        [(i, 8) for i in range(6, 24)] + \
#     #                        [(i, 9) for i in range(11)]

#     #     for (x, y) in tree_coordinates:
#     #         # Create and place a TreeAgent
#     #         tree_agent = TreeAgent((x, y), self)
#     #         self.grid.place_agent(tree_agent, (x, y))
#     #         self.schedule.add(tree_agent)
            
            
#     def create_trees(self, tree_ranges):
#         """Add trees to the grid  with parameters - tree ranges : a list of tuples, which each start and end points"""
#         for start_point, end_point in tree_ranges:
#          start_x, start_y = start_point
#          end_x, end_y = end_point

#         for x in range (start_x, end_x + 1):  # This should be inside the previous loop
#          for y in range (start_y, end_y + 1):
#           tree_agent = TreeAgent((x,y), self)
#         self.grid.place_agent(tree_agent, (x,y))
#         self.schedule.add(tree_agent)

             
             
             
#              #moved above in class farmMOdel 
#         # tree_ranges = [
#         #     ((0, 0), (22, 0)),     # first range - column 0 from row 0 to 22     #row,column format 
#         #     ((3, 2), (24, 2)),     # second range - column 2 from row 3 to 24
#         #     ((0, 4), (13, 4)),     # 
#         #     ((15, 4), (21, 4)),
#         #     ((6, 8), (23, 8)),
#         #     ((0, 9), (10, 9))
             
#         # ]
             
#         # self.create_trees(tree_ranges)
             
             
            
        
        
        
        
        
        
            
# #TODO : simplify the function and create a loop with start point and end point 
    
#     # def create_crops(self):
#     #     """
#     #     Add crop agents to the grid at predefined coordinates.
#     #     """
#     #     crops_coordinates = [(0, 0), (13, 4), (14, 4), (2, 8), (3, 8), (4, 8), (16, 10), (17, 10)]
        
        
#     #     for (x, y) in crops_coordinates:
#     #         crop_agent = CropAgent((x, y), self)
#     #         self.grid.place_agent(crop_agent, (x, y))
#     #         self.schedule.add(crop_agent)



#     def create_crops(self, crops_coordinates):
#         """ Add crops to the grid with specified coordinates ( a list of tuples representing crop locations)"""
#         for (x,y) in crops_coordinates:
#             crop_agent = CropAgent((x,y), self)
#             self.grid.place_agent(crop_agent, (x,y))
#             self.schedule.add(crop_agent)
            
         
         
#          #moved above in class FarmModel 
#         # crops_coordinates = [(0, 0), (13, 4), (14, 4), (2, 8), (3, 8), (4, 8), (16, 10), (17, 10)]
        
#         # self.crate_crops(crops_coordinates)
        
        

#     # def create_path(self):
#     #     """
#     #     Add path agents to the grid at predefined coordinates.
#     #     """
#     #     path_coordinates = [(i, 1) for i in range(25)]  # Vertical column at 1
        
#     #     for (x, y) in path_coordinates:
#     #         path_agent = PathAgent((x, y), self)
#     #         self.grid.place_agent(path_agent, (x, y))
#     #         self.schedule.add(path_agent)

    
    
#     def create_path(self, start_point, end_point):
#         """Add path to the grid within specified ranges """
#         start_x, start_y = start_point
#         end_x, end_y = end_point
        
#         for x in range(start_x, end_x + 1):
#          for y in range(start_y , end_y + 1):
#              path_agent = PathAgent((x,y) , self)
#              self.grid.place_agent(path_agent, (x,y))
#              self.schedule.add(path_agent)
             
             
#         # self.create_path(start_point=(1,0), end_point= (1,24))

     

# class WaterAgent(Agent):
#     def __init__(self, pos, model):
#         """
#         Initialize a WaterAgent.
#         """
#         super().__init__(pos, model)
#         self.type = "water"

# class TreeAgent(Agent):
#     def __init__(self, pos, model):
#         """
#         Initialize a TreeAgent.
#         """
#         super().__init__(pos, model)
#         self.type = "tree"


# class CropAgent(Agent):
#     def __init__(self, pos, model):
#         super().__init__(pos, model)
#         self.type = "crop"
        
        
# class PathAgent(Agent):
#     def __init__(self, pos, model):
#         super().__init__(pos, model)
#         self.type = "path"








from mesa import Model, Agent
from mesa.space import MultiGrid
from mesa.time import BaseScheduler
#import improtlib 
#import random
#importlib.reload(agents)
from agents import PickerRobot



class FarmModel(Model):
    def __init__(self, width= 100, height=100, num_robots = 2):
        """
        Initialize the farm model with the given width and height.
        """
        super().__init__()  # Explicitly initialize the Model class
        self.grid = MultiGrid(width, height, torus=False)  # Non-toroidal grid
        self.schedule = BaseScheduler(self)  # Scheduler for agents



        # Terrain setup
        tree_ranges = [
    ((0, 1), (0, 24)),  # Trees along the first row
    ((2, 3), (2, 24)),  # Trees in a vertical column
    ((4, 0), (4, 13)),  # Trees in a vertical column
    ((4, 15), (4, 21)), # Separate section for trees
    ((8, 6), (8, 23)),  # Trees in another column
    ((9, 0), (9, 10)),  # Final range of trees
]


        # Add terrain agents
        self.create_water(start_point=(6,0), end_point=(6,24))
        self.create_trees(tree_ranges)
        self.create_crops([
            (4,13), (4,14), (2, 8), (3, 8), (4, 8), (10,16), (10,17)
        ])
        self.create_path(start_point=(1, 0), end_point=(1, 24))
        self.create_base()
        
        
        #add picker robot
        for i in range (num_robots):
            x = self.random.randint(0, width -1)
            y = self.random.randint(0, height - 1)
            while not self.grid.is_cell_empty((x,y)):
                x = self.random.randint(0, width -1)
                y = self.random.randint(0, height - 1)
            print(f"Creating PickerRobot with id = {self.next_id()}, pos = {(x,y)}, model={self}")     #debug print for arguments passed to pickerrobot in the farmmodel constructor
            picker_robot = PickerRobot (self.next_id(), (x,y), self)
            self.grid.place_agent(picker_robot, (x,y))
            self.schedule.add(picker_robot)
            

                
                

    def create_water(self, start_point, end_point):
        start_x, start_y = start_point
        end_x, end_y = end_point
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                print(f"Placing WaterAgent at ({x}, {y})")
                water_agent = WaterAgent((x, y), self)
                self.grid.place_agent(water_agent, (x, y))
                self.schedule.add(water_agent)

    def create_trees(self, tree_ranges):
        for start_point, end_point in tree_ranges:
            start_x, start_y = start_point
            end_x, end_y = end_point
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    print(f"Placing TreeAgent at ({x}, {y})")
                    tree_agent = TreeAgent((x, y), self)
                    self.grid.place_agent(tree_agent, (x, y))
                    self.schedule.add(tree_agent)

    def create_crops(self, crops_coordinates):
        for (x, y) in crops_coordinates:
            print(f"Placing CropAgent at ({x}, {y})")
            crop_agent = CropAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(crop_agent, (x, y))
            self.schedule.add(crop_agent)

    def create_path(self, start_point, end_point):
        start_x, start_y = start_point
        end_x, end_y = end_point
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                print(f"Placing PathAgent at ({x}, {y})")
                path_agent = PathAgent((x, y), self)
                self.grid.place_agent(path_agent, (x, y))
                self.schedule.add(path_agent)
                
                
                
    def create_base(self):
        """
        Add base station to the grid along the column = 0 
        """
        base_position = (0, 0) 
        print(f"Base position: {base_position}")
        base_agent = BaseAgent(base_position, self)
        self.grid.place_agent(base_agent, base_position)
        self.schedule.add(base_agent)
        
    def step(self):
        self.schedule.step()
        
        


class WaterAgent(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.type = "water"


class TreeAgent(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.type = "tree"


class CropAgent(Agent):
    def __init__(self, _id, pos, model):
        super().__init__(_id, model)
        self.type = "crop"
        self.pos = pos


class PathAgent(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.type = "path"


class BaseAgent(Agent):
    def __init__(self, pos, model):
        super(). __init__(pos, model)
        self.type = "base"
        
        
# class PickerRobot(Agent):
#     def __init__(self, pos, model):
#         super().__init__(pos, model)
#         self.type= "picker_robot"
        
        
## important !!! to get the model started 
def step(self):
    """ 
    Advance the model by one step. 
    """
    print("Advancing the model by oen step.")    #debugging 
    self.schedule.step()     #triggers all agents step methods 
    