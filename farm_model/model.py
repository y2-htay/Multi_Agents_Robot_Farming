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
        #New Coordinates    # old one also in a loop range , but different coordinates , called in function as the same way 
#         tree_ranges = [
#     ((0, 2), (0, 3)), # Range for trees in the first column
#     ((0,6), (0,11)),
#     ((0,14),(0,19)),
#     ((0,21),(0,22)),
#     ((0,24),(0,24),
#      (()))
#     ((1, 2), (1, 6)),   # Range for trees in the second column
#     ((4, 0), (4, 13)),  # Range for trees in the fifth column
#     ((8, 2), (8, 7)),   # Range for trees in the ninth column
#     ((16, 2), (16, 18)), # Range for trees in the seventeenth column
#     ((20, 0), (20, 19)), # Range for trees in the twenty-first column
#     ((24, 2), (24, 24)), # Range for trees in the last column
#     # Add more ranges as needed
# ]
        # tree_coordinates = [
        #     (0, 2), (1, 2), (4, 0), (8, 2), (16, 2), (20, 0), (24, 2),
        #     (0, 3), (1, 3), (4, 1), (8, 3), (16, 3), (20, 1), (24, 3),
        #     (1, 4), (4, 2), (8, 4), (16, 4), (20, 2), (24, 4),
        #     (1, 5), (4, 3), (8, 5),
        #     (0, 6), (1, 6), (4, 4), (8, 6),
        #     (0, 7), (8, 7), (16, 7), (20, 5), (24, 7),
        #     (0, 8), (16, 8), (20, 6), (24, 8),
        #     (0, 9), (4, 7), (8, 9), (20, 7), (24, 9),
        #     (0, 10), (1, 10), (4, 8), (8, 10), (16, 10), (20, 8), (24, 10),
        #     (0, 11), (1, 11), (4, 9), (16, 11), (20, 9),
        #     (1, 12), (4, 10), (8, 12), (16, 12), (20, 10),
        #     (1, 13), (4, 11), (8, 13), (16, 13), (20, 11), (24, 13),
        #     (0, 14), (1, 14), (4, 12), (8, 14), (20, 12), (24, 14),
        #     (0, 15), (1, 15), (4, 13), (8, 15), (24, 15),
        #     (0, 16), (1, 16), (4, 14), (8, 16), (16, 16), (20, 14),
        #     (0, 17), (1, 17), (8, 17), (16, 17), (20, 15), (24, 17),
        #     (0, 18), (1, 18), (16, 18), (20, 16), (24, 18),
        #     (0, 19), (1, 19), (4, 17), (20, 17), (24, 19),
        #     (1, 20), (4, 18), (20, 18), (24, 20),
        #     (0, 21), (1, 21), (4, 19), (8, 21), (16, 21), (20, 19),
        #     (0, 22), (1, 22), (4, 20), (8, 22), (16, 22), (20, 20),
        #     (1, 23), (8, 23), (24, 23),
        #     (0, 24), (1, 24), (4, 22), (8, 24), (16, 24), (20, 22), (24, 24),
        #     (5, 0), (9, 2), (5, 10),
        #     (5, 1), (17, 3), (21, 1), (5, 11),
        #     (5, 2), (17, 4), (21, 2), (5, 12),
        #     (5, 3), (9, 5), (17, 5), (21, 3), (5, 15),
        #     (5, 4), (9, 6), (17, 6), (21, 4), (5, 16),
        #     (5, 5), (9, 7), (17, 7), (21, 5), (5, 21),
        #     (5, 6), (9, 8), (17, 8), (21, 6), (9, 23),
        #     (5, 7), (9, 9),
        #     (5, 8), (9, 10), (17, 10), (21, 8),
        #     (5, 9), (9, 11), (17, 11), (21, 9),
        #     (9, 12),
        #     (9, 13), (17, 13), (21, 11),
        #     (9, 14), (17, 14), (21, 12),
        #     (5, 13), (17, 15),
        #     (5, 14), (9, 16), (17, 16), (21, 14),
        #     (9, 17), (17, 17), (21, 15),
        #     (9, 18), (17, 18), (21, 16),
        #     (5, 17), (9, 19), (21, 17),
        #     (5, 18), (9, 20),
        #     (5, 19), (9, 21), (17, 21),
        #     (5, 20), (9, 22), (17, 22), (21, 20),
        #     (21, 21),
        #     (5, 22), (9, 24), (17, 24), (21, 22)
        # ]

        
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
                
        
        
        
        
        ###New path Coordinates 
#         path_coordinates = [
#     (2, 0), (3, 0), (4, 23), (6, 0), (7, 0), (8, 0), (10, 0), (11, 0), (12, 23), (14, 0), (15, 0), (16, 0), 
#     (18, 0), (19, 0), (20, 23), (22, 0), (23, 0), (24, 0),
#     (2, 1), (3, 1), (4, 24), (6, 1), (7, 1), (8, 1), (10, 1), (11, 1), (12, 24), (14, 1), (15, 1), (16, 1), 
#     (18, 1), (19, 1), (20, 24), (22, 1), (23, 1), (24, 1),
#     ...
#     (2, 24), (3, 24), (6, 24), (7, 24), (10, 24), (11, 24), (14, 24), (15, 24), (18, 24), (19, 24), (22, 24), (23, 24)
# ]
        
        
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
        


        






        
        
    
    #     #old tree ranges 
    #     tree_ranges = [
    # ((0, 1), (0, 24)),  # Trees along the first row
    # ((2, 3), (2, 24)),  # Trees in a vertical column
    # ((4, 0), (4, 13)),  # Trees in a vertical column
    # ((4, 15), (4, 21)), # Separate section for trees
    # ((8, 6), (8, 23)),  # Trees in another column
    # ((9, 0), (9, 10)),  # Final range of trees



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
        
        
        
        
        
        # #add picker robot
        # for i in range (num_robots):
        #     x = self.random.randint(0, width -1)
        #     y = self.random.randint(0, height - 1)
            
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
    def create_crops(self, crops_coordinates):
        for (x, y) in crops_coordinates:
            print(f"Placing CropAgent at ({x}, {y})")
            crop_agent = CropAgent(self.next_id() ,(x, y), self)
            #crop_agent = CropAgent(self.next_id,(x,y), self)
            self.grid.place_agent(crop_agent, (x, y))
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
        
    # def step(self):
    #     self.schedule.step()
    

    
    #New function for base with 4 coordinates ,
    def create_base(self, base_coordinates):
        for (x, y) in base_coordinates:
            print(f"Placing BaseAgent at ({x}, {y})")
            base_agent = BaseAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(base_agent, (x, y))
            self.schedule.add(base_agent)
            self.pos = (x,y)
        
        


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
    