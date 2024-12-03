#supress futurewarning from mesa (agentset warningS)
import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)


# Import the server from server.py
from server import server



# Run the server
if __name__ == "__main__":
    server.port = 8523
    print("Starting the server....")
    server.launch()






### TODO:  Robots making a way back to base in a pattern 
    # Djoikstra's algorithm
    #station name--> tuples()
    #covert the tuples into strings
    #store the hash in place of the station
    #when making the hash, also save the


## TODO: Communication of drones and pickers 

   ## Drones Send signals to picker robots 
   ## individually 
   ## to all pickers 
   ## picker leaves the base once the drone  send a signal with crops coordinates 

## TODO: 
   
    
   
    
  


  ### TODO:  
  ## Stop pickers and robots from going to base unless they need ( storage full or  battery dies)
 
  ## Picker stop when storage is full (Done)

  ## Drone battery dies test (Done)

  ## two drones at one crop #both wait until the picker comes 

  ## dynamic arrowhead for drone (Done)






  ## TODO: Optional 

  ## stages of fruit - no crop, green , yellow , ripe 

  ## check network 

  ## expand the reach ,, neighbors 

  ## make_decision needed in drones ? 

  ## so battery is not based on individual move, its just all about step?

  ## strawberry regrowth 



  ## CHECKLIST : 

  ## Drones move in 6 directions , front , back , left , right , up , down 

  ## Pickers move past water ( reduced speed ? )

  ## 