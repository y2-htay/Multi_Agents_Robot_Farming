# from mesa.visualization.ModularVisualization import ModularServer
# from mesa.visualization.modules import CanvasGrid
# from model import FarmModel
# from portrayal import farm_portrayal

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from model import FarmModel
from portrayal import farm_portrayal

# Set up the grid visualization
canvas_element = CanvasGrid(farm_portrayal, 25, 25, 600, 600)

# Initialize the server
server = ModularServer(
    FarmModel,  # Model class
    [canvas_element],  # Visualization elements
    "Farm Simulation",  # Title of the simulation
    {"width": 25, "height": 25, "num_robots": 2}  # Model parameters
)
