#supress futurewarning from mesa (agentset warningS)
import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)
 # Import the server from server.py
from farm_model.server import server



# Run the server
if __name__ == "__main__":
    server.port = 8523
    print("Starting the server....")
    server.launch()
