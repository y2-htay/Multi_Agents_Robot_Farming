#supress futurewarning from mesa (agentset warningS)
import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)
 # Import the server from server.py
from server import server



# Run the server
if __name__ == "__main__":
    server.port = 8524
    print("Starting the server....")
    server.launch()
