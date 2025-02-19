import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)
from mesa import Model, Agent
from mesa.space import MultiGrid
from mesa.time import BaseScheduler
from farm_model.agents import PickerRobot, ExtendedPicker
from farm_model.agents import DroneRobot, ExtendedDrone



#############################################################
           ### Farm Model Class Initialisation
#############################################################


class FarmModel(Model):
    def __init__(self, width= 29, height=25, num_drones = 2, num_pickers = 2, mode = "Basic", movement = "random"):
        """
        Initialize the farm model with the given width and height.
        """
        super().__init__()  # Explicitly initialize the Model class
        print("Initialising FarmModel......")   #debug
        self.grid = MultiGrid(width, height, torus=False)  # Non-toroidal grid
        self.schedule = BaseScheduler(self)  # Scheduler for agents
        #self.mode = "basic"
        self.mode = mode
        self.step_count = 0     # initialise step counter 
        self.movement = "random"
        



#############################################################
           ### Terrain Coordinates Definition 
#############################################################



        #Terrain Setup
        tree_ranges = [
    ((0, 2), (0,24)),
    ((1,2), (1,24)),
    ((2,2), (2,24)),   #new tree line
    #((4,0), (4,22)),
    ((5,0), (5,22)),
    ((6,0), (6,22)),
    ((7,0),(7,22)),   #new tree line 
    #((8,2), (8,24)),
    #((9,2), (9,24)),
    ((10,2), (10,24)),
    ((11,2), (11,24)),
    ((12,2), (12,24)),  # new tree line 
    ((21,0), (21,22)),
    ((22,0), (22,22)),
    ((23,0), (23,22)),
    ((26,2), (26,24)),
    ((27,2), (27,24)),
    ((28,2),  (28,24))
       # new tree line
    
]
        
        
        #New Water Coordinates
        water_ranges = [(x, y) for x in [15,16,17,18] for y in range(25)]
        
        

        crops_coordinates = [
        (0,4),(1,4),(2,4)  , (0,5),(1,5),(2,5), (0,8),(1,8),(2,8), (0,12),(1,12),(2,12),(0,13),(1,13),(2,13),(0,18),(1,18),(2,18),(0,20),(1,20),(2,20), (0,23),(1,23),(2,23),(5,2),(6,2),(7,2),(5,5),(6,5),(7,5),(5,6),(6,6),(7,6),(5,10),(6,10),(7,10),(5,11),(6,11),(7,11),(5,15),(6,15),(7,15),
        (5,16),(6,16),(7,16),(5,21),(6,21),(7,21),(10,3),(11,3),(12,3),(10,4),(11,4),(12,4),(10,8),(11,8),(12,8),(10,11),(11,11),(12,11),(10,14),(11,14),(12,14),(10,19),(11,19),(12,19),(10,20),(11,20),(12,20),(10,23),(11,23),(12,23),(21,0),(22,0),(23,0),(21,3),(22,3),(23,3),(21,4),(22,4),(23,4),
        (21,7),(22,7),(23,7),(21,10),(22,10),(23,10),(21,13),(22,13),(23,13),(21,18),(22,18),(23,18),(21,19),(22,19),(23,19),(21,21),(22,21),(23,21),(26,2),(27,2),(28,2),(26,3),(27,3),(28,3),(26,8),(27,8),(28,8),(26,9),(27,9),(28,9),(26,12),(27,12),(28,12),(26,15),(27,15),(28,15),(26,16),(27,16),(28,16),
        (26,19),(27,19),(28,19),(26,20),(27,20),(28,20),(26,24),(27,24),(28,24)
]
                
        
        #New base now with four coordinates /four cell grids 
        base_coordinates = [
    (0, 0), (0, 1), (1, 0), (1, 1), (2,0),(2,1)
]
        
        
        #Generating the coordinates in a loop rather than defining all these 
        path_coordinates =[]
        
        # Example: Generate paths along specific columns or rows
        for x in [ 3,4,8,9, 13,14,19,20,24,25]:
            for y in range(25):  # Assuming 0-24 rows
                path_coordinates.append((x, y))

        # Adding specific points like (4, 23), (12, 23), etc.
        path_coordinates.extend([(2,0), (2,1),(4, 23), (4, 24) , (5,23), (5,24), (6,23), (6,24),(7,23),(7,24), (8,0), (8,1), (9,0),(9,1),(10,0), (10,1),(11,0),(11,1), (12,0), (12,1), (21,23),(22,23),(23,23),(21,24),(22,24),(23,24),(26,0),(27,0),(28,0),(26,1),(27,1),(28,1)])
        


#############################################################
           ### Calling terrain functions
#############################################################


        # Add terrain agents
       # self.create_water(start_point=(6,0), end_point=(6,24))
        #print("Setting up water...")
        self.create_water(water_ranges)      #for new water coordinates loop 
        #print("Water setup complete.")
        self.create_trees(tree_ranges)
        #print("Tree setup complete.")
        self.create_crops(crops_coordinates)     #for new coordinates   # created a list of coordinates separate instead of calling in the function 
        #print("Crop setup complete.")
        self.create_path(path_coordinates)      #for new path coordinates;
        #print("Path setup complete.")
        self.create_base(base_coordinates)
        #print("Base setup complete.")
        
    



##########################################################
  #### Call the appropriate robot placement method based on the mode
##########################################################


        if self.mode == "Basic":
            print("Starting basic robot placement...")
            self.basic_robot_placement(num_drones, num_pickers)
        elif self.mode == "Extended":
            print("Starting extended robot placement...")
            self.extended_robot_placement(num_drones, num_pickers)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")


###########################################################
######  Basic Mode Drone and Picker Placement 
###########################################################


    def basic_robot_placement(self, num_drones, num_pickers):
        print("Starting basic robot placement...")

        """Place drones and pickers randomly on the grid."""


        for i in range(num_drones):
            print(f"Attempting to place DroneRobot {i}...")
            x = self.random.randint(0, self.grid.width - 1)
            y = self.random.randint(0, self.grid.height - 1)
            drone_robot = DroneRobot(self.next_id(), (x, y), self)
            self.grid.place_agent(drone_robot, (x, y))
            self.schedule.add(drone_robot)
            print(f"DroneRobot {i} placed at {(x, y)}.")




            #Placing pickers ranomly -- For basic operation    #difference to last one working with battery 
        #robot placement anywhere apart from water and tree grids   ## works works works this one works 
        for i in range(num_pickers):
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



###########################################################
###### Extended Mode Drone and Picker Placement 
###########################################################



    base_coordinates = [
        (0, 0), (0, 1), (1, 0), (1, 1), (2,0),(2,1)
    ]

    def extended_robot_placement(self, num_drones, num_pickers):
            print("Extended Robots  placed.")
            """Place drones and pickers at the base."""
            for i in range(num_drones):
                if not self.base_coordinates:
                    print("No more available base cells for drones.")
                    break
                x, y = self.random.choice(self.base_coordinates)
                drone_robot = ExtendedDrone(self.next_id(), (x, y), self)
                self.grid.place_agent(drone_robot, (x, y))
                self.schedule.add(drone_robot)

            for i in range(num_pickers):
                if not self.base_coordinates:
                    print("No more available base cells for pickers.")
                    break
                x, y = self.random.choice(self.base_coordinates)
                picker_robot = ExtendedPicker(self.next_id(), (x, y), self)
                self.grid.place_agent(picker_robot, (x, y))
                self.schedule.add(picker_robot)
            


#############################################################
           ##Functions for Terrains
#############################################################
    

    #######################
      ##  Water Function
    #######################



    def create_water(self, water_coordinates):
        for (x,y) in water_coordinates:
            #print (f"Placing WaterAgent at ({x}, {y})")
            water_agent = WaterAgent(self.next_id() ,(x,y), self)
            self.grid.place_agent(water_agent, (x,y))
            self.schedule.add(water_agent)
                    

     

    #######################
      ##  Tree Function
    #######################


    #for new tree ranges
    def create_trees(self, tree_ranges):
        for start_point, end_point in tree_ranges:
            start_x, start_y = start_point
            end_x, end_y = end_point
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    tree_agent = TreeAgent(self.next_id(), (x,y), self)
                    self.grid.place_agent(tree_agent, (x,y))
                    self.schedule.add(tree_agent)
    
    
            
            
    #######################
      ## Crop Function 
    #######################
    
    def create_crops(self, crops_coordinates):
        for (x, y) in crops_coordinates:
            # Check if the cell contains a TreeAgent
            existing_agents = self.grid.get_cell_list_contents((x, y))
            has_tree = any(isinstance(agent, TreeAgent) for agent in existing_agents)
            
            if not has_tree:
                # Skip this position if there is no tree
                continue 
            
            # Place the CropAgent with the default stage as "mature"
            crop_agent = CropAgent(self.next_id(), (x, y), self, growth_stage = "mature")
            self.grid.place_agent(crop_agent, (x, y))
            self.schedule.add(crop_agent)

    
            
    #######################
      ##  Path Function
    #######################


    
    #New function for path coordinates defined in a list path_coordinates  , and called  in function self.create_path(path_coordinates)      
    def create_path(self, path_coordinates):
        for (x,y) in path_coordinates:
            #print(f"Placing PathAgent at ({x}, {y})")
            path_agent = PathAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(path_agent, (x, y))
            self.schedule.add(path_agent)
            
    #######################
      ##  Base Function
    #######################


    #New function for base with 4 coordinates ,
    def create_base(self, base_coordinates):
        for (x, y) in base_coordinates:
            #print(f"Placing BaseAgent at ({x}, {y})")
            base_agent = BaseAgent(self.next_id() ,(x, y), self)
            self.grid.place_agent(base_agent, (x, y))
            self.schedule.add(base_agent)
            self.pos = (x,y)
            


#############################################################
           ### MODEL SIMULATION
#############################################################

    
    #######################
      ##  Step Function
    #######################


    """ Farm Model Simulation starts here """
    def step(self):
        print(f"Model starts here")
        print(f"Step {self.step_count}.......")
        self.schedule.step()
        self.step_count += 1      # increment step counter




#############################################################
           ### Classes for terrains 
#############################################################

class BaseTerrains(Agent):
    def __init__(self, _id, pos, model):
        super().__init__( _id, model)
        self.pos = pos


class WaterAgent(BaseTerrains):   #an agent representing a tree on the grid 
    def __init__(self, _id, pos, model):
        super().__init__( _id, pos, model)
        #self.type = "water"
        #self.pos = pos


class TreeAgent(BaseTerrains):
    def __init__(self, _id ,pos,  model):
        super().__init__(_id, pos, model)
        #self.type = "tree"
        #self.pos = pos


class CropAgent(BaseTerrains):
    def __init__(self,  _id, pos, model, growth_stage = "mature"):
        super().__init__( _id,pos,  model)    #pos not needed to be passed 
        #self.type = "crop"
        #self.pos = pos
        self.growth_stage = growth_stage  # default stage -> mature for originally located crops
        self.crop_timer = 0       #timer for advancing crop age 
        self.growth_stages = ["seed", "immature", "mature"]      # crop stages 
        self.color = self.get_color()       
        
    

    def get_color(self):
        """ Return the right color of stage to the crop"""
        if self.growth_stage == "seed":
            return "gray"
        elif self.growth_stage == "immature":
            return "yellow"
        elif self.growth_stage == "mature":
            return "red"
        
    

    def reset_crop_stage(self):
        """ Reset the crop to its seed stage """
        #if self.growth_stage == "mature": 
        self.growth_stage = "seed"
        self.crop_timer = 0 
        self.color = self.get_color()   # update color 
        print (f"Crop at {self.pos} has been reset to seed stage with color {self.color} .")



    def step(self):
        """Advance the crop's growth stage based on the timer"""
        self.crop_timer += 1

        if self.growth_stage == "seed" and self.crop_timer>=35:
            self.growth_stage = "immature"     # = error lol
            self.color = self.get_color()    # update color
            self.crop_timer = 0 
            print(f"Crop at {self.pos} transitioned from seed to immature with color{self.color}.")


        elif self.growth_stage == "immature" and self.crop_timer >= 50:
            self.growth_stage = "mature"
            self.color = self.get_color()    #update color 
            self.crop_timer = 0 
            print(f"Crop at {self.pos} transitioned from immature to mature stage with color {self.color}.") 



class PathAgent(BaseTerrains):
    def __init__(self, _id, pos, model):
        super().__init__( _id,pos,  model)
        #self.type = "path"
        #self. pos = pos 
        

class BaseAgent(BaseTerrains):
    def __init__(self,  _id, pos, model):
        super(). __init__( _id, pos, model)
        #self.type = "base"
        #self.pos = pos
        

        

    


################################################

###############################################



        

    