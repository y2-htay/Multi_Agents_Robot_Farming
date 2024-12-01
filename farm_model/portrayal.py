from model import WaterAgent, TreeAgent, CropAgent, PathAgent, BaseAgent, PickerRobot

def farm_portrayal(agent):
    """
    Determine the portrayal based on the agent's type.
    """
    # if isinstance(agent, PickerRobot) or isinstance(agent, DroneRobot):
    #     return robot_portrayal(agent)
    if isinstance (agent, PickerRobot):
        return {
            "Shape": "circle",
            #"Color" : "white" if agent.is_busy else "orange", 
            "Color" : "white",
            "Filled" : "true",
            "Layer" : 2,
            "r" : 0.7,
            # "x": agent.pos[0],
            # "y": agent.pos[1],
            
        }
    if isinstance(agent, WaterAgent):
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

# def robot_portrayal(robot):
#     """
#     Portrayal for robots (PickerRobot and DroneRobot).
#     """
#     return {
#         "Shape": "circle",
#         "r": 0.7,
#         "Layer": 2,
#         "Color": "red" if robot.type == "picker_robot" else "purple",
#         "x": robot.pos[0],
#         "y": robot.pos[1],
#     }

def water_portrayal(water):
    """
    Portrayal for WaterAgent.
    """
    if water is None:
        raise AssertionError
    return {
        "Shape": "rect",
        "Color": "blue",
        "Layer": 0,
        "Filled": "true",
        "w": 1,
        "h": 1,
        #"scale": 2,
        #"x": water.pos[0],
        #"y": water.pos[1],
    }

def tree_portrayal(tree):
    """
    Portrayal for TreeAgent.
    """
    if tree is None:
        raise AssertionError
    return {
        "Shape": "rect",
        "Color": "green",
        "Layer": 0,
        "w": 1,
        "h": 1,
        "Filled": "true",
        #"x": tree.pos[0],
        #"y": tree.pos[1],
    }

def crop_portrayal(crop):
    """
    Portrayal for CropAgent.
    """
    if crop is None:
        raise AssertionError
    return {
        "Shape": "circle",
        "Color": "orange",
        "Layer": 1,
        "r": 0.7,
        "Filled": "true",
        #"x": crop.pos[0],
        #"y": crop.pos[1],
    }

def path_portrayal(path):
    """
    Portrayal for PathAgent.
    """
    if path is None:
        raise AssertionError
    return {
        "Shape": "rect",
        "Color": "brown",
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
        "Color": "purple",
        "Layer": 0,
        "w": 1,
        "h": 1,
        "Filled": "true",
        
    }
    
    
    
# def picker_robot_portrayal(picker_robot):
#     """ 
#     Portrayal for PickerRobot
#     """
#     if picker_robot is None:
#         raise AssertionError
#     return {
#         "Shape": "circle",
#         "Color": "red" if picker_robot.is_busy else "green",
#         "Layer": 2,
#         "r": 0.7,
#         "Filled": "true",
#     }
    