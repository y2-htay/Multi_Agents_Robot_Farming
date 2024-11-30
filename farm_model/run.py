# Import the server from server.py
from server import server

# Run the server
if __name__ == "__main__":
    server.port = 8524
    server.launch()
