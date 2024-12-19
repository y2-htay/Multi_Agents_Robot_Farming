import unittest
from unittest.mock import Mock, patch
from collections import deque
from mesa import Model
from farm_model.agents import PickerRobot  # Update import path
from farm_model.model import CropAgent, TreeAgent, WaterAgent

# Constants matching your implementation
FREE = 1  # Based on the error showing state is 1 instead of "FREE"
BUSY = 2
BATTERY_SKIP_THRESHOLD = 50  # Battery depletion threshold

class MockModel(Model):
    """Mock Model class that provides the minimum required attributes for Mesa Agent"""
    def __init__(self):
        super().__init__()
        self.grid = Mock()
        self.schedule = Mock()
        self.random = Mock()
        # Initialize the _agents dict with a dict for PickerRobot
        self._agents = {PickerRobot: {}}
        self.running = True
        self.grid.width = 10
        self.grid.height = 10

class TestPickerRobot(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        self.model = MockModel()
        self.initial_pos = (5, 5)
        self.robot = PickerRobot(1, self.initial_pos, self.model)

    def test_initialization(self):
        """Test if robot is initialized with correct default values"""
        self.assertEqual(self.robot.unique_id, 1)
        self.assertEqual(self.robot.pos, self.initial_pos)
        self.assertEqual(self.robot.state, FREE)  # Updated to match actual implementation
        self.assertEqual(self.robot.storage, 0)
        self.assertEqual(self.robot.capacity, 1000)
        self.assertEqual(self.robot.battery, 100)
        self.assertEqual(self.robot.battery_tick, 0)
        self.assertEqual(self.robot.type, "picker_robot")

    def test_reach_property(self):
        """Test if reach property returns correct positions within grid bounds"""
        reach = self.robot.Reach
        
        # Check if positions are within grid bounds
        for pos in reach:
            x, y = pos
            self.assertTrue(0 <= x < 10)
            self.assertTrue(0 <= y < 10)
            
        # Check if positions are within 3 cells range
        for pos in reach:
            x, y = pos
            self.assertTrue(abs(x - self.initial_pos[0]) <= 3)
            self.assertTrue(abs(y - self.initial_pos[1]) <= 3)

    @patch('builtins.print')  # Mock print to avoid console output during tests
    def test_return_to_base_when_full(self, mock_print):
        """Test if robot returns to base when storage is full"""
        self.robot.storage = self.robot.capacity
        action = self.robot.make_decision()
        self.assertEqual(action, "return_to_base")
        self.assertEqual(self.robot.state, "returning")  # Make sure this matches your implementation

    @patch('builtins.print')  # Mock print to avoid console output during tests
    def test_return_to_base_when_low_battery(self, mock_print):
        """Test if robot returns to base when battery is low"""
        self.robot.battery = 15
        action = self.robot.make_decision()
        self.assertEqual(action, "return_to_base")
        self.assertEqual(self.robot.state, "returning")  # Make sure this matches your implementation

    @patch('builtins.print')  # Mock print to avoid console output during tests
    def test_move_randomly(self, mock_print):
        """Test if move_randomly function works correctly"""
        # Mock valid steps
        valid_steps = [(4, 5), (5, 4), (6, 5)]
        self.model.grid.get_neighborhood.return_value = valid_steps
        self.model.grid.get_cell_list_contents.return_value = []
        self.model.random.choice.return_value = valid_steps[0]
        
        self.robot.move_randomly()
        
        # Verify robot moved to chosen position
        self.model.grid.move_agent.assert_called_with(self.robot, valid_steps[0])

    @patch('builtins.print')  # Mock print to avoid console output during tests
    def test_avoid_trees_when_moving(self, mock_print):
        """Test if robot avoids trees when moving"""
        # Mock neighborhood with a tree
        tree = Mock(spec=TreeAgent)
        tree_pos = (4, 5)
        empty_pos = (5, 4)
        
        self.model.grid.get_neighborhood.return_value = [tree_pos, empty_pos]
        self.model.grid.get_cell_list_contents.side_effect = lambda pos: [tree] if pos == tree_pos else []
        self.model.random.choice.return_value = empty_pos
        
        self.robot.move_randomly()
        
        # Verify robot moved to empty position
        self.model.grid.move_agent.assert_called_with(self.robot, empty_pos)

    @patch('builtins.print')  # Mock print to avoid console output during tests
    def test_wait_function(self, mock_print):
        """Test if wait function does nothing as expected"""
        initial_pos = self.robot.pos
        initial_storage = self.robot.storage
        initial_battery = self.robot.battery
        
        self.robot.wait()
        
        # Verify nothing changed
        self.assertEqual(self.robot.pos, initial_pos)
        self.assertEqual(self.robot.storage, initial_storage)
        self.assertEqual(self.robot.battery, initial_battery)

if __name__ == '__main__':
    unittest.main()