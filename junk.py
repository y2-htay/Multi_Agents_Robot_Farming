#################################################################################################################################################################################################


################################# from model.py  ######################################################



################################################################################################################################################################################################






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







 # #add picker robot  ( locate for the initial grid ) 
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





                 
    ##debug                
    # def place_agent_safe(self, agent, position):
    #     # Check if the agent is already at the position
    #     if self.grid.is_agent_at(position):  # Assuming you have a method to check this
    #         current_agent = self.grid.get_agent_at(position)  # Get the current agent at the position
    #         self.grid.remove_agent(current_agent)  # Remove the agent from its current position
    #     self.grid.place_agent(agent, position)  # Now place the new agent safely   










# def step(self):
    #     print ("Advancing the model by one step")
    #     self.schedule.step()    

        
    # ##debug - works
    # def log_cell_contents(self):
    #     """ Log the contents of each cell in the grid."""
    #     for x in range(self.grid.width):
    #         for y in range(self.grid.height):
    #             contents = self.grid.get_cell_list_contents((x,y))
    #             if contents:
    #                 print(f"Cell ({x},{y}) contains: {[type(agent).__name__ for agent in contents]}")
    #             if any(isinstance(agent, PickerRobot) for agent in contents):
    #                 print(f"PickerRobot located at ({x}, {y})")
                    




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








### Debug : log the grid contents after initialisation
        #self.log_cell_contents()
        
        ##debug: placing robots in random grid without constraints 
        # for i in range(num_robots):
        #     x = self.random.randint(0, self.grid.width -1)
        #     y = self.random.randint(0, self.grid.height -1)
        #     picker_robot = PickerRobot(self.next_id(), (x,y), self)
        #     self.grid.place_agent(picker_robot, (x,y))
        #     self.schedule.add(picker_robot)
        #     print(f"PickerRobot {picker_robot.unique_id} placed at ({x}, {y})"




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









################################################################################################################################################################################################


################################# from server  ######################################################



################################################################################################################################################################################################







############ Server.py##############




### debugging server ######
# from mesa import Model
# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid
# from mesa.space import MultiGrid
# from mesa.time import BaseScheduler
# from mesa import Agent

# class MinimalAgent(Agent):
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)

# class MinimalModel(Model):
#     def __init__(self):
#         self.grid = MultiGrid(10, 10, False)
#         self.schedule = BaseScheduler(self)
#         agent = MinimalAgent(1, self)
#         self.grid.place_agent(agent, (5, 5))

# def minimal_portrayal(agent):
#     return {"Shape": "circle", "Color": "blue", "r": 0.5, "Layer": 1}

# grid = CanvasGrid(minimal_portrayal, 10, 10, 500, 500)
# server = ModularServer(MinimalModel, [grid], "Minimal Model", {})
# server.port = 8524
# server.launch()




# ## debug - standalone grid test 

# from mesa import Model
# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid
# from mesa.space import MultiGrid
# from mesa.time import BaseScheduler
# from mesa import Agent

# class MinimalAgent(Agent):
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)

# class MinimalModel(Model):
#     def __init__(self):
#         self.grid = MultiGrid(10, 10, False)
#         self.schedule = BaseScheduler(self)
#         agent = MinimalAgent(1, self)
#         self.grid.place_agent(agent, (5, 5))

# def minimal_portrayal(agent):
#     return {"Shape": "circle", "Color": "blue", "r": 0.5, "Layer": 1}

# grid = CanvasGrid(minimal_portrayal, 10, 10, 500, 500)
# server = ModularServer(MinimalModel, [grid], "Minimal Model", {})
# server.port = 8524
# server.launch()







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



 
################################################################################################################################################################################################


################################# from portrayal ######################################################



################################################################################################################################################################################################


######### Portral.py ##################################


# def robot_portrayal(robot):
#     """
#     Portrayal for robots (PickerRobot and DroneRobot).
#     """
#     return {
#         "Shape": "circle",
#         "r": 0.7,
#         "Layer": 2,
#         "Color": "red" if robot.type == "picker_robot" else "purple",
#         "x": robot.pos[0],
#         "y": robot.pos[1],
#     }








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









################################################################################################################################################################################################


################################# from agents ######################################################



################################################################################################################################################################################################
























# ################ New Drones ########################


# class DroneRobot(Agent):
#     """Drones"""
#     def __init__(self, unique_id, pos, model):
#         print(f"Initialising the drone robot with {unique_id}, {pos}, {model}")
#         super().__init__(unique_id, model)
#         self.pos = pos
#         self.state = "idle"      ## "idle" or "searching"
#         self.battery =  100
#         self.battery_tick = 0
#         self.type =  "drone_robot"
#         #for dynamic arrow 
#         self.prev_pos = pos # Track previous position ( # for dynamic heading )
#         self.heading = (0,0)


#     # Dynamic Arrowhead (new )
#     def arrow_step(self):
#         """update position and heading dynamically for the arrow"""
#         #from mesa.space import MultiGrid     #ensuring grid handling works correctly


#         p_x, p_y = self.prev_pos
#         c_x, c_y = self.pos
        
#         if (p_x < c_x):
#             self.heading = (1,0)
#         elif (p_x > c_x):
#             self.heading = (-1,0)
#         elif (p_y < c_y):
#             self.heading = (0,1)
#         elif (p_y > c_y):
#             self.heading = (0,-1)
#          # Debugging
#         print(f"Drone {self.unique_id}: Prev Pos = {self.prev_pos}, Current Pos = {self.pos}, Heading = {self.heading}")




    
#     @property 
#     def is_busy(self):
#         return self.state == BUSY
    

# ###############step function for drones##############

#     def step


    




##########  Return to base using dijkstra algorithm ####################
### needs to be outside the class ,: python treats it as a method requiring a self argument , 
# @staticmethod
# def dijkstra(grid, start, goal):
#        """
#        Dijkstra's Algorithm for finding the shortest path in a grid.
#        :param grid: The grid (MultiGrid object from Mesa).
#        :param start: Start position (x, y).
#        :param goal: Goal position (x, y).
#        :return: List of positions representing the shortest path.
#        """
#        # Priority queue for Dijkstra
#        queue = [(0, start)]  # (cost, position)
#        visited = set()
#        came_from = {}
#        cost_so_far = {start: 0}

#        while queue:
#            current_cost, current_pos = heapq.heappop(queue)

#            if current_pos in visited:
#                continue
#            visited.add(current_pos)

#            # Stop if we reach the goal
#            if current_pos == goal:
#                break

#            # Get neighbors
#            x, y = current_pos
#            neighbors = [
#                (x + dx, y + dy)
#                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Von Neumann neighborhood
#                if 0 <= x + dx < grid.width and 0 <= y + dy < grid.height
#            ]

#            for neighbor in neighbors:
#                # Assume cost of moving is 1 (adjust for terrain if needed)
#                new_cost = current_cost + 1

#                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
#                    cost_so_far[neighbor] = new_cost
#                    priority = new_cost
#                    heapq.heappush(queue, (priority, neighbor))
#                    came_from[neighbor] = current_pos

#        # Reconstruct path
#        path = []
#        current = goal
#        while current != start:
#            path.append(current)
#            current = came_from.get(current, start)
#        path.reverse()

#        return path




#############################################################
#            ### Make Decison Function(picker) original working main one before , adding return_to_base function 
# ############################################################

  
#     def make_decision(self):
#         """ 
#         Decide the next action based on the robot's state and surrondings.
#         """
#         print(f"PickerRobot {self.unique_id} is making a decision.")
#         from model import CropAgent     
        
#         if self.battery == 0 :
#             print(f"Picker battery died.")
#             return "wait"
        
        
#         # new added for capacity storage check 
#         if self.storage >= 1000:     #for inidvidual or both ?
#             print(f"Storage Full for PickerRobot")
#             return "wait" 
            
#         if self.state == FREE:
#             #Check if there is a cropagent nearby (ignore treeagent )
#             crop_nearby = any(
#                 isinstance(agent, CropAgent)
#                 for agent in self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 3)
#             )
#             print(f"PickerRobot {self.unique_id} Crop Nearby: {crop_nearby}")
#             return "pick" if crop_nearby else "move_randomly"
#         elif self.state == BUSY:
#             return "return_to_base" if self.storage >= self.capacity else "move_randomly"
#         else:
#             return "wait" 
        




#############################################################
           ### Make Decison Function(picker)   Test for returning to base 
#############################################################
    
    # def make_decision(self):
    #     """ 
    #     Decide the next action based on the robot's state and surrondings.
    #     """
    #     print(f"PickerRobot {self.unique_id} is making a decision.")
    #     from model import CropAgent     
        
    #     if self.battery == 0 :
    #         print(f"Picker battery died.")
    #         return "return_to_base"
        
        
    #     # new added for capacity storage check 
    #     if self.storage >= 5:     #for inidvidual or both ?
    #         print(f"Storage Full for PickerRobot")
    #         return "return to base" 
            
    #     if self.state == FREE:
    #         #Check if there is a cropagent nearby (ignore treeagent )
    #         crop_nearby = any(
    #             isinstance(agent, CropAgent)
    #             for agent in self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 3)
    #         )
    #         print(f"PickerRobot {self.unique_id} Crop Nearby: {crop_nearby}")
    #         return "pick" if crop_nearby else "move_randomly"
    #     elif self.state == BUSY:
    #         return "return_to_base" if self.storage >= self.capacity else "move_randomly"
    #     else:
    #         return "wait"    
        


# -----------------------------------------------

#############################################################
           ### step function (picker ) Test for return to base 
#############################################################
    
    # def step(self):
    #     """ 
    #     Define the behaviour of the robot at each step 
    #     """
    #     print(f"PickerRobot {self.unique_id} is stepping at position {self.pos}.")
    #     print("battery for ", self.unique_id, " = ", self.battery)
    #     print("Storage for", self.unique_id, "=", self.storage)

        
    #     #decrease battery level every few ticks 
    #     self.battery_tick += 1
        
    #     if self.battery_tick == BATTERY_SKIP_THRESHOLD:
    #         self.battery_tick = 0
    #         self.battery -= 1
            
        
    #     print(f"PickerRobot {self.unique_id} is taking a step at position {self.pos}.") #debug
    #     #Decision making 
    #     action = self.make_decision()
    #     print(f"PickerRobot {self.unique_id} decided to : {action }")     #debug print for the visual movement of pickerrobot 
    #     getattr(self,action)()        #execuse the chosen action 

# ---------------------------------------
    # def step(self):
    #   """
    #   Define the behavior of the robot at each step.
    #   """
    #   print(f"PickerRobot {self.unique_id} is stepping at position {self.pos}.")
    #   print(f"Battery for {self.unique_id}: {self.battery}, Storage: {self.storage}")

    #   # Decrease battery level every few ticks
    #   self.battery_tick += 1
    #   if self.battery_tick == BATTERY_SKIP_THRESHOLD:
    #       self.battery_tick = 0
    #       self.battery -= 1

    #   # Make a decision and execute the corresponding action
    #   action = self.make_decision()
    #   print(f"PickerRobot {self.unique_id} decided to: {action}")
    #   getattr(self, action)()





















### not working 
    # def return_to_base(self):
    #     """ 
    #     Move toward to the base to drop off crops       ( battery charging to be added later )
    #     """
    #     ##debug
    #     print(f"picker robot is returning to base")
    #     base_x, base_y = 0,0  
    #     current_x, current_y = self.pos
    #     dx = base_x - current_x      ##????
    #     dy = base_y - current_y 
    #     move_x = current_x +  ( 1 if dx > 0 else -1 if dx < 0 else 0 )
    #     move_y = current_y +  (1 if dy > 0 else -1 if dy < 0 else 0 )
    #     new_position = (move_x, move_y)
    #     if self.model.grid.is_cell_empty(new_position):
    #         self.model.grid.move_agent(self, new_position)
            



    #--------------------------
    #### not working 
    # def return_to_base(self):
    #     """ 
    #     Move toward the base (0, 0) step by step to drop off crops.
    #     """
    #     base_x, base_y = 0, 0  # Base coordinates
    #     current_x, current_y = self.pos

    #    # Debugging output
    #     print(f"PickerRobot {self.unique_id} at {self.pos} returning to base at {(base_x, base_y)}")

    #    # Determine the direction to move in each axis
    #     dx = base_x - current_x
    #     dy = base_y - current_y

    #    # Calculate next step coordinates
    #     next_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
    #     next_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)

    #    # Check valid moves in each direction
    #     possible_moves = [
    #        (next_x, current_y),  # Move horizontally
    #        (current_x, next_y),  # Move vertically
    #     ]

    #    # Filter valid moves (inside grid and unoccupied)
    #     valid_moves = [
    #        move for move in possible_moves
    #        if (
    #           0 <= move[0] < self.model.grid.width and
    #           0 <= move[1] < self.model.grid.height and
    #           self.model.grid.is_cell_empty(move)
    #         )
    #     ]   

    #     if  valid_moves:
    #         # Choose the first valid move
    #         new_position = valid_moves[0]
    #         print(f"PickerRobot {self.unique_id} moving from {self.pos} to {new_position}.")
    #         self.model.grid.move_agent(self, new_position)
    #     else:
    #         print(f"PickerRobot {self.unique_id} cannot move to base; all possible moves are blocked.")



####-----------------------------------------------

    
    # #### return to base without constraints (working )
    # def return_to_base(self):
    #    """
    #    Move toward the base (0, 0) using Dijkstra's Algorithm to find the shortest path.
    #    """
    #    base_x, base_y = 0, 0  # Base coordinates
    #    current_pos = self.pos

    #    # Find the shortest path
    #    path = dijkstra(self.model.grid, current_pos, (base_x, base_y))

    #    if not path:
    #        print(f"PickerRobot {self.unique_id} cannot find a path to the base.")
    #        return

    #    # Move one step along the path
    #    next_step = path[0]  # Take the first step toward the base
    #    print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_step}.")
    #    self.model.grid.move_agent(self, next_step)
    #    #self.add.grid.schedule(PickerRobot)
      

####-----------------------------------------------
    #### return to base avoiding constraints (slowdown in water and avoid trees - not working )
    # def return_to_base(self):
    #   """ 
    #   Move toward the base (0, 0) step by step, avoiding trees and slowing down near water.
    #   """
    #   from model import TreeAgent, WaterAgent  # Import dependencies

    #   base_x, base_y = 0, 0  # Base coordinates
    #   current_x, current_y = self.pos

    #   # Debugging
    #   print(f"PickerRobot {self.unique_id} at {self.pos} returning to base at {(base_x, base_y)}")

    #   # If the robot is slowed down by water, skip this step
    #   if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0:
    #       print(f"PickerRobot {self.unique_id} is slowing down near water.")
    #       self.slowdown_counter -= 1
    #       return

    #   # Calculate movement direction
    #   dx = base_x - current_x
    #   dy = base_y - current_y
    #   next_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
    #   next_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)

    #   # Create a list of potential steps toward the base
    #   possible_steps = [
    #       (next_x, current_y),  # Horizontal move
    #       (current_x, next_y)   # Vertical move
    #   ]

    #   # Filter out invalid steps (trees and out-of-bounds cells)
    #   valid_steps = [
    #       step for step in possible_steps
    #       if (
    #           0 <= step[0] < self.model.grid.width and
    #           0 <= step[1] < self.model.grid.height and
    #           not any(isinstance(a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))
    #       )
    #   ]

    #   if valid_steps:
    #       # Select the first valid step (prioritizes moving closer to the base)
    #       new_position = valid_steps[0]

    #       # Check if the new position contains water
    #       if any(isinstance(a, WaterAgent) for a in self.model.grid.get_cell_list_contents(new_position)):
    #           print(f"PickerRobot {self.unique_id} entering water at {new_position}.")
    #           self.slowdown_counter = 5  # Slow down for 5 steps

    #       # Move to the new position
    #       print(f"PickerRobot {self.unique_id} moving from {self.pos} to {new_position}.")
    #       self.model.grid.move_agent(self, new_position)
    #   else:
    #       print(f"PickerRobot {self.unique_id} cannot move to base; all possible moves are blocked.")


######################## return to base using breadth first search ########################
##########################################################################################
#     from collections import deque

#     def find_path_around_trees(grid, start, goal):
#       """
#       Breadth-First Search (BFS) to find a path avoiding trees, designed for Mesa's MultiGrid.
#       """
#       from model import TreeAgent

#       queue = deque([(start, [])])  # (current_position, path_taken)
#       visited = set()

#       while queue:
#           current, path = queue.popleft()

#           # If we've reached the goal, return the path
#           if current == goal:
#               return path + [current]

#           # Mark the current position as visited
#           visited.add(current)

#           # Get neighbors in the grid
#           x, y = current
#           neighbors = [
#               (x + dx, y + dy)
#               for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Von Neumann neighborhood
#               if 0 <= x + dx < grid.width and
#                  0 <= y + dy < grid.height and
#                  (x + dx, y + dy) not in visited and
#                  not any(isinstance(agent, TreeAgent) for agent in grid.get_cell_list_contents((x + dx, y + dy)))
#           ]

#           # Add neighbors to the queue
#           for neighbor in neighbors:
#               queue.append((neighbor, path + [current]))

#       # If no path is found
#       return []

    
# ## return 
#     def return_to_base(self):
#       """
#       Move toward the base (0, 0) step by step, avoiding trees and slowing down near water.
#       Designed for Mesa's MultiGrid and agent behavior.
#       """
#       from model import WaterAgent

#       base_x, base_y = 0, 0  # Base coordinates
#       current_pos = self.pos

#       # If the robot is slowed down by water, skip this step
#       if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0:
#           print(f"PickerRobot {self.unique_id} is slowing down near water.")
#           self.slowdown_counter -= 1
#           return

#       # Find a path avoiding trees
#       path = self.find_path_around_trees(self.model.grid, current_pos, (base_x, base_y))

#       if not path:
#           print(f"PickerRobot {self.unique_id} cannot find a path to the base.")
#           return

#       # Move one step along the path
#       next_step = path[0]
#       print(f"PickerRobot {self.unique_id} moving from {self.pos} to {next_step}.")

#       # Check if the new position contains water
#       if any(isinstance(agent, WaterAgent) for agent in self.model.grid.get_cell_list_contents(next_step)):
#           print(f"PickerRobot {self.unique_id} entering water at {next_step}.")
#           self.slowdown_counter = 5  # Slow down for 5 steps

#       # Move the robot
#       self.model.grid.move_agent(self, next_step)

############## return to base ( shadowed form move randomly )
    

    ### works( avoiding trees and slowing down in water ) but not efficient , - not prioritizing the way back , 
    # def return_to_base(self):
    #   """
    #   Move toward the base to drop off crops, avoiding trees and slowing down in water.
    #   """
    #   from model import TreeAgent, WaterAgent

    #   # Define the base coordinates
    #   base_x, base_y = 0, 0  # Assuming base is at (0, 0)

    #   # Get current position
    #   current_x, current_y = self.pos

    #   # Calculate the direction to move toward the base
    #   dx = base_x - current_x
    #   dy = base_y - current_y

    #   # Normalize the direction to a single step
    #   move_x = current_x + (1 if dx > 0 else -1 if dx < 0 else 0)
    #   move_y = current_y + (1 if dy > 0 else -1 if dy < 0 else 0)
    #   new_position = (move_x, move_y)

    #   # Get the possible steps (Moore neighborhood)
    #   possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)

    #   # Filter valid steps (avoid trees)
    #   valid_steps = [step for step in possible_steps if not any(isinstance(a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))]

    #   # Check if the new position is valid
    #   if new_position in valid_steps:
    #       # Check if the new position contains water to slow down
    #       if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0:
    #           print(f"PickerRobot {self.unique_id} is slowing down near the water.")
    #           self.slowdown_counter -= 1
    #           return  # Skip this step

    #       if any(isinstance(a, WaterAgent) for a in self.model.grid.get_cell_list_contents(new_position)):
    #           print(f"PickerRobot {self.unique_id} entering water at {new_position}.")
    #           self.slowdown_counter = 5  # Slow down for 5 steps

    #       # Move the robot to the new position
    #       print(f"PickerRobot {self.unique_id} moving from {self.pos} to {new_position}.")
    #       self.model.grid.move_agent(self, new_position)
    #       print(f"PickerRobot {self.unique_id} moved to {new_position}.")
    #   else:
    #       print(f"PickerRobot {self.unique_id} cannot move directly to {new_position}, finding an alternative path.")
    #       # Choose an alternative valid step randomly
    #       if valid_steps:
    #           alternative_position = self.random.choice(valid_steps)
    #           if any(isinstance(a, WaterAgent) for a in self.model.grid.get_cell_list_contents(alternative_position)):
    #               print(f"PickerRobot {self.unique_id} entering water at {alternative_position}.")
    #               self.slowdown_counter = 5  # Slow down for 5 steps

    #           self.model.grid.move_agent(self, alternative_position)
    #           print(f"PickerRobot {self.unique_id} moved to {alternative_position}.")



    ##### not working #####
    # def return_to_base(self):
    #   """
    #   Move toward the base to drop off crops, avoiding trees and slowing down in water.
    #   """
    #   from model import TreeAgent, WaterAgent

    #   # Define the base coordinates
    #   base_x, base_y = 0, 0  # Assuming base is at (0, 0)

    #   # Get the current position
    #   current_x, current_y = self.pos

    #   # Get all possible steps (Moore neighborhood)
    #   possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)

    #   # Filter out steps blocked by trees
    #   valid_steps = [step for step in possible_steps if not any(isinstance(a, TreeAgent) for a in self.model.grid.get_cell_list_contents(step))]

    #   if not valid_steps:
    #       print(f"PickerRobot {self.unique_id} is stuck and cannot move.")
    #       return  # No valid moves available

    #   # Calculate the Manhattan distance to the base for each valid step
    #   valid_steps_with_distance = [(step, abs(base_x - step[0]) + abs(base_y - step[1])) for step in valid_steps]

    #   # Sort steps by distance to the base (ascending)
    #   valid_steps_with_distance.sort(key=lambda x: x[1])

    #   # Choose the step that brings the robot closest to the base
    #   best_step = valid_steps_with_distance[0][0]

    #   # If the best step contains water, slow down
    #   if hasattr(self, 'slowdown_counter') and self.slowdown_counter > 0:
    #       print(f"PickerRobot {self.unique_id} is slowing down near water.")
    #       self.slowdown_counter -= 1
    #       return  # Skip this step

    #   if any(isinstance(a, WaterAgent) for a in self.model.grid.get_cell_list_contents(best_step)):
    #       print(f"PickerRobot {self.unique_id} entering water at {best_step}.")
    #       self.slowdown_counter = 5  # Slow down for 5 steps

    #   # Move the robot to the best step
    #   print(f"PickerRobot {self.unique_id} moving from {self.pos} to {best_step}.")
    #   self.model.grid.move_agent(self, best_step)
    #   print(f"PickerRobot {self.unique_id} moved to {best_step}.")









































 # crops = [ a for a in self.model.grid.get_cell_list_contents(each)if isinstance (a, CropAgent)]
            # if crops:
            #     crop = crops[0]
            #     self.model.grid.remove_agent(crop)
            #     self.storage += 1
            #     print(f"Picked a strawberry at {each} . Storage: {self.storage}")








#temporary function to test random movement of the robots without constrainst , no restrictions to water and  trees.
    # def move_randomly(self):
    #     """
    #     Move the robot to a random neighboring cell, without any restrictions.
    #     """
    #     print(f" PickerRobot {self.unique_id} attempting to move.")   #debug
    #     possible_steps = self.model.grid.get_neighborhood(
    #         self.pos, moore = True, include_center = False 
    #     )
    #     if possible_steps:
    #         new_position = self.random.choice(possible_steps)
    #         print(f"PickerRobot {self.unique_id} moving from {self.pos} to {new_position}.")
    #         self.model.grid.move_agent(self, new_position)
    #     else:
    #         print(f"PickerRobot {self.unique_id} moved to {new_position}")     #debug 




###################function after battery ############cuuu
        
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


###### debug , test for step , robots movement without constraints ######
    # def step(self):
    #     """ Test robots movement by calling move_randomly """
    #     print(f"PickerRobot {self.unique_id} stepping at position {self.pos}.")
    #     self.move_randomly()
        
    #def advance(self) -> None:
        
       
            
        # if self.battery < 1:
        #     return
    
    
    
    ###########
    













# def step(self):
    #   print(f"PickerRobot {self.unique_id} stepping at position {self.pos}.")
    #   self.move_randomly()


   
                
                
                
    #             positions.append((c_x + x, c_y + y))
                
    #     return positions















 #reach property checking positions outside of the grid too 
    # def Reach(self) -> list:
    #     #make list of positions to return
    #     #take current position
    #     # for ever quare that this can reach
    #     # add the offset position to the list
    #     positions = []
    #     c_x, c_y = self.pos
    #     for x in range(-3, 4):
    #         for y in range (-3, 4):
    #             if c_x + x < 0:
    #                 continue
    #             if c_x + x > self.model.grid.width:
    #                 continue
    #             if c_y + y < 0 :
    #                 continue
    #             if c_y + y > self.model.grid.height:
    #                 continue





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
    















################################################################################################################################################################################################


################################# from agents ######################################################



################################################################################################################################################################################################











# ## checking the server with minimal agent , for debug  --> if this works the issue is in FarmModel.
# from mesa import Model
# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid
# from mesa.space import MultiGrid
# from mesa.time import BaseScheduler
# from mesa import Agent

# # Minimal Agent
# class MinimalAgent(Agent):
#     def __init__(self, unique_id, model):
#         super().__init__(unique_id, model)

# # Minimal Model
# class MinimalModel(Model):
#     def __init__(self):
#         self.grid = MultiGrid(10, 10, False)
#         self.schedule = BaseScheduler(self)

# # Minimal portrayal function
# def minimal_portrayal(agent):
#     return {"Shape": "circle", "Color": "blue", "r": 0.5, "Layer": 1}

# # Set up server
# grid = CanvasGrid(minimal_portrayal, 10, 10, 500, 500)
# server = ModularServer(MinimalModel, [grid], "Minimal Model", {})
# server.port = 8524
# server.launch()


# ##Debug -- to test the server without visualisation , 
# from model import FarmModel

# if __name__ == "__main__":
#     model = FarmModel(width=25, height=25, num_robots=2)
#     print("Running model...")
#     for i in range(10):
#         print(f"Step {i}")
#         model.step()
