# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid
# from model import FarmModel
# from portrayal import farm_portrayal

import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from model import FarmModel
from portrayal import farm_portrayal

# Set up the grid visualization
print("Setting up CanvasGrid....")      # debug
canvas_element = CanvasGrid(farm_portrayal, 25, 25, 600, 600)


print(f"Initialising the ModularServer....")  #debug
# Initialize the server
server = ModularServer(
    FarmModel,  # Model class
    [canvas_element],  # Visualization elements
    "Farm Simulation",  # Title of the simulation
    {"width": 25, "height": 25, "num_robots": 2}  # Model parameters
)

#debug
print("Server is ready.")



