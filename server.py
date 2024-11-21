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
    {"width": 25, "height": 25}  # Model parameters
)
