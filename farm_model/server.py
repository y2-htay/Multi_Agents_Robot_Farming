# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid
# from model import FarmModel
# from portrayal import farm_portrayal

import warnings
from mesa.visualization import Slider
from mesa.visualization import Choice
warnings.filterwarnings("ignore", category  = FutureWarning)
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from model import FarmModel
from portrayal import farm_portrayal

# Set up the grid visualization
print("Setting up CanvasGrid....")      # debug
canvas_element = CanvasGrid(farm_portrayal, 29, 25, 609, 600)




simulation_params = {
    "width": 29,
    "height": 25,
    "mode": Choice(
        'My Choice',
        value='Default choice',
        choices=['Basic', 'Extended']
    ),
    "num_robots": Slider(
        'number of robots',
        2, #default
        1, #min
        10, #max
        1, #step
        
        
        "choose how many robots to include in the simulation"
    )}


print(f"Initialising the ModularServer....")  #debug
# Initialize the server
server = ModularServer(
    FarmModel,  # Model class
    [canvas_element],  # Visualization elements
    "Farm Simulation",  # Title of the simulation
    #{"width": 29, "height": 25, "num_robots": 2}  # Model parameters
    simulation_params,
)

#debug
print("Server is ready.")



