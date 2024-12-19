import unittest
import mesa
from mesa import Model
from farm_model.agents import  DroneRobot, PickerRobot, ExtendedDrone, ExtendedPicker
from farm_model.model import TreeAgent, WaterAgent, CropAgent, PathAgent, BaseAgent

class TestFarmModel(unittest.TestCase):
    def setUp(self):
        """Set up a FarmModel instance for testing."""
        from farm_model.model import FarmModel  # Import here to avoid circular import
        self.model = FarmModel(width=29, height=25, num_drones=2, num_pickers=2, mode="Basic")

    def test_initialization(self):
        """Test basic initialization of the FarmModel."""
        # Check model is an instance of Model
        self.assertIsInstance(self.model, Model)
        
        # Check grid properties
        self.assertEqual(self.model.grid.width, 29)
        self.assertEqual(self.model.grid.height, 25)
        self.assertFalse(self.model.grid.torus)

    def test_terrain_creation(self):
        """Test creation of different terrain agents."""
        # Check water agents
        water_agents = [agent for agent in self.model.schedule.agents if isinstance(agent, WaterAgent)]
        self.assertTrue(len(water_agents) > 0)
        
        # Check tree agents
        tree_agents = [agent for agent in self.model.schedule.agents if isinstance(agent, TreeAgent)]
        self.assertTrue(len(tree_agents) > 0)
        
        # Check crop agents
        crop_agents = [agent for agent in self.model.schedule.agents if isinstance(agent, CropAgent)]
        self.assertTrue(len(crop_agents) > 0)
        
        # Check path agents
        path_agents = [agent for agent in self.model.schedule.agents if isinstance(agent, PathAgent)]
        self.assertTrue(len(path_agents) > 0)
        
        # Check base agents
        base_agents = [agent for agent in self.model.schedule.agents if isinstance(agent, BaseAgent)]
        self.assertTrue(len(base_agents) > 0)

    def test_robot_placement_basic_mode(self):
        """Test robot placement in Basic mode."""
        # Test drone robots
        drone_robots = [agent for agent in self.model.schedule.agents if isinstance(agent, DroneRobot)]
        self.assertEqual(len(drone_robots), 2)
        
        # Test picker robots
        picker_robots = [agent for agent in self.model.schedule.agents if isinstance(agent, PickerRobot)]
        self.assertEqual(len(picker_robots), 2)

    def test_robot_placement_extended_mode(self):
        """Test robot placement in Extended mode."""
        from farm_model.model import FarmModel
        extended_model = FarmModel(width=29, height=25, num_drones=2, num_pickers=2, mode="Extended")
        
        # Test extended drone robots
        extended_drones = [agent for agent in extended_model.schedule.agents if isinstance(agent, ExtendedDrone)]
        self.assertEqual(len(extended_drones), 2)
        
        # Test extended picker robots
        extended_pickers = [agent for agent in extended_model.schedule.agents if isinstance(agent, ExtendedPicker)]
        self.assertEqual(len(extended_pickers), 2)

    def test_invalid_mode(self):
        """Test that an invalid mode raises a ValueError."""
        from farm_model.model import FarmModel
        with self.assertRaises(ValueError):
            FarmModel(width=29, height=25, num_drones=2, num_pickers=2, mode="Invalid")

    def test_crop_placement_with_trees(self):
        """Test that crops are only placed on cells with trees."""
        crop_agents = [agent for agent in self.model.schedule.agents if isinstance(agent, CropAgent)]
        
        for crop in crop_agents:
            # Get the cell contents where the crop is placed
            cell_contents = self.model.grid.get_cell_list_contents(crop.pos)
            
            # Check that there's at least one TreeAgent in the cell
            tree_in_cell = any(isinstance(agent, TreeAgent) for agent in cell_contents)
            self.assertTrue(tree_in_cell, f"Crop at {crop.pos} is not on a cell with a tree")

    def test_base_coordinates(self):
        """Test the base coordinates are correct."""
        expected_base_coords = {(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)}
        base_agents = [agent for agent in self.model.schedule.agents if isinstance(agent, BaseAgent)]
        
        # Collect actual base coordinates
        actual_base_coords = {agent.pos for agent in base_agents}
        
        # Check that the actual base coordinates match the expected ones
        self.assertEqual(actual_base_coords, expected_base_coords)

if __name__ == '__main__':
    unittest.main()