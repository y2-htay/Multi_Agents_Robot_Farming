######
##From Model.py




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





########



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
        
        
        
        
        
        ###New path Coordinates 
#         path_coordinates = [
#     (2, 0), (3, 0), (4, 23), (6, 0), (7, 0), (8, 0), (10, 0), (11, 0), (12, 23), (14, 0), (15, 0), (16, 0), 
#     (18, 0), (19, 0), (20, 23), (22, 0), (23, 0), (24, 0),
#     (2, 1), (3, 1), (4, 24), (6, 1), (7, 1), (8, 1), (10, 1), (11, 1), (12, 24), (14, 1), (15, 1), (16, 1), 
#     (18, 1), (19, 1), (20, 24), (22, 1), (23, 1), (24, 1),
#     ...
#     (2, 24), (3, 24), (6, 24), (7, 24), (10, 24), (11, 24), (14, 24), (15, 24), (18, 24), (19, 24), (22, 24), (23, 24)
# ]
        
    
        
    
    #     #old tree ranges 
    #     tree_ranges = [
    # ((0, 1), (0, 24)),  # Trees along the first row
    # ((2, 3), (2, 24)),  # Trees in a vertical column
    # ((4, 0), (4, 13)),  # Trees in a vertical column
    # ((4, 15), (4, 21)), # Separate section for trees
    # ((8, 6), (8, 23)),  # Trees in another column
    # ((9, 0), (9, 10)),  # Final range of trees

















############ Server.py##############


# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid, ChartModule
# from model import FarmModel  # Import your FarmModel class
# from portrayal import farm_portrayal  # Import the portrayal function

# # Grid configuration
# grid_width = 11
# grid_height = 25

# # Define the CanvasGrid module with the portrayal function
# grid = CanvasGrid(farm_portrayal, grid_width, grid_height, 500, 500)  # 500x500 px display

# # Optional: Add a chart to track metrics like the number of watered crops
# chart = ChartModule(
#     [{"Label": "WateredCrops", "Color": "yellow"}],  # Example metric
#     #data_collector_name="datacollector"
# )

# # Create the ModularServer
# server = ModularServer(
#     FarmModel,  # The model class
#     [grid, chart],  # Visualization elements
#     "Farm Simulation",  # Title of the simulation
#     {"width": grid_width, "height": grid_height}  # Model parameters
# )

# # # Launch the server
# # if __name__ == "__main__":
# #     server.launch()





#Make a world that is 50x50, on a 250x 250 display, 
# import mesa
# from model import  FarmModel
# from portrayal import farm_portrayal
# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid






# print(FarmModel)
# #make a world that is 50x50 , on a 250x250 diaplay
# canvas_element = CanvasGrid(farm_portrayal, 11,25,250,250)

# print(canvas_element)
# server = ModularServer (
#     FarmModel,[canvas_element],
#     "Farm Simulation",
#     {"width" : 11 , "height" : 25 }
# )



 



######### Portral.py ##################################




# def farm_portrayal(agent):
#     """
#     Map agents to their visual representation.
#     """
#     portrayal = {}

#     # WaterAgent portrayal
#     if agent.type == "WaterAgent":
#         portrayal = {
#             "Shape": "rect",
    #         "Color": "blue",
    #         "Layer": 0,
    #         "w": 1,
    #         "h": 1
    #     }

    # # TreeAgent portrayal
    # elif agent.type == "tree":
    #     portrayal = {
    #         "Shape": "rect",
    #         "Color": "green",
    #         "Layer": 1,
    #         "w": 1,
    #         "h": 1
    #     }

    # # PathAgent portrayal
    # elif agent.type == "path":
    #     portrayal = {
    #         "Shape": "rect",
    #         "Color": "brown",
    #         "Layer": 0,
    #         "w": 1,
    #         "h": 1
    #     }

    # # CropAgent portrayal
    # elif agent.type == "crop":
    #     portrayal = {
    #         "Shape": "circle",
    #         "Color": "yellow",
    #         "Layer": 2,
    #         "r": 0.5
    #     }

    # return portrayal





########## from agents #####


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
    