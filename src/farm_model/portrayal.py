import warnings
warnings.filterwarnings("ignore", category  = FutureWarning)
from .model import WaterAgent, TreeAgent, CropAgent, PathAgent, BaseAgent
from .model import PickerRobot, DroneRobot, ExtendedPicker, ExtendedDrone

def farm_portrayal(agent):
    """
    Determine the portrayal based on the agent's type.
    """
    if isinstance (agent, (PickerRobot, ExtendedPicker)):
        return {
            "Shape": "circle",
            #"Color" : "white" if agent.is_busy else "orange", 
            "Color" : "white",
            "Filled" : "true",
            "r": 0.7,
            "Layer" : 2,
            "id": agent.unique_id
         
        }
    if isinstance(agent, (DroneRobot, ExtendedDrone)):
        return drone_robot_portrayal(agent)
    elif isinstance(agent, WaterAgent):
        return water_portrayal(agent)
    elif isinstance(agent, TreeAgent):
        return tree_portrayal(agent)
    elif isinstance(agent, CropAgent):
        return crop_portrayal(agent)
    elif isinstance(agent, PathAgent):
        return path_portrayal(agent)
    elif isinstance(agent, BaseAgent):
        return base_portrayal(agent)
    # elif isinstance(agent, PickerRobot):
    #     return picker_robot_portrayal(agent)
    else:
        return {"Shape": "rect", "Color": "gray", "Layer": 0, "w": 1, "h": 1}



def water_portrayal(water):
    """
    Portrayal for WaterAgent.
    """
    if water is None:
        raise AssertionError
    return {
        "Shape": "rect",
        "Color": "#1E90FF",  #seawater
        "Layer": 0,
        "Filled": "true",
        "w": 1,
        "h": 1,
     
    }

def tree_portrayal(tree):
    """
    Portrayal for TreeAgent.
    """
    if tree is None:
        raise AssertionError
    return {
        "Shape": "rect",
        "Color": "#228B22",  # forest green 
        "Layer": 0,
        "w": 1,
        "h": 1,
        "Filled": "true",
     
    }



####################################
    #### Crop portrayl with aging  
####################################

def crop_portrayal(crop):
    """
    Portrayal for CropAgent based on its growth stage.
    """
    if crop is None:
        raise AssertionError

    color_map = {
        "seed": "gray",  # Light yellow   "#FFFF99"
        "immature": "yellow",  # Orange    "#FFA500"
        "mature": "red",  # Green (default for current crops)   #008000"
    }

    return {
        "Shape": "circle",
        "Color": color_map.get(crop.growth_stage, "red"),  # Default to mature color
        "Layer": 1,
        "r": 0.8,
        "Filled": "true",
    }


def path_portrayal(path):
    """
    Portrayal for PathAgent.
    """
    if path is None:
        raise AssertionError
    return {
        "Shape": "rect",
        "Color": "#8B4513",   
        "Layer": 0,
        "w": 1,
        "h": 1,
        "Filled": "true",
        #"x": path.pos[0],
        #"y": path.pos[1],
    }



def base_portrayal(base):
    """ 
    Portrayal for BaseAgent
    """
    if base is None:
        raise AssertionError
    return {
        "Shape": "rect",
        #"Color": "#DA70D6",  #orchid purple
        "Color" : "black" ,
        "Layer": 0,
        "w": 1,
        "h": 1,
        "Filled": "true",
        
    }
    
    


def drone_robot_portrayal(agent):
    """ Portrayal for DroneRobot as an arrowhead """
    if isinstance(agent, DroneRobot):
        heading_x, heading_y = agent.heading if hasattr(agent, "heading") else (0,0)
        if heading_x == 0 and heading_y == 0 :
            heading_x, heading_y = 0, 1  #default to pointing up if no movement
        return {
            "Shape" : "arrowHead",
            "Color" : "cyan",
            "Filled" : "true",
            "Layer" : 2,
            "scale" : 0.7, 
            "heading_x": heading_x, 
            "heading_y" : heading_y, 
            "id": agent.unique_id
        }

