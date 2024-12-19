import unittest
from unittest.mock import Mock, patch
from mesa import Model
from farm_model.agents import DroneRobot  # Update import 
from farm_model.model import CropAgent, TreeAgent

class MockModel(Model):
    """Mock Model class that provides the minimum required attributes for Mesa Agent"""
    def __init__(self):
        super().__init__()
        self.grid = Mock()
        self.schedule = Mock()
        self.random = Mock()
        # Initialize the _agents dict with a dict for DroneRobot
        self._agents = {DroneRobot: {}}
        self.running = True
        self.grid.width = 10
        self.grid.height = 10

class TestDroneRobot(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        self.model = MockModel()
        self.initial_pos = (5, 5)
        self.drone = DroneRobot(1, self.initial_pos, self.model)

    def test_initialization(self):
        """Test if drone is initialized with correct default values"""
        self.assertEqual(self.drone.unique_id, 1)
        self.assertEqual(self.drone.pos, self.initial_pos)
        self.assertEqual(self.drone.state, "searching")
        self.assertEqual(self.drone.battery, 100)
        self.assertEqual(self.drone.battery_tick, 0)
        self.assertEqual(self.drone.type, "drone_robot")
        self.assertEqual(self.drone.prev_pos, self.initial_pos)
        self.assertEqual(self.drone.heading, (0, 0))
        self.assertEqual(self.drone.signal_queue, [])
        self.assertIsNone(self.drone.picker_id_waiting)

    @patch('builtins.print')
    def test_arrow_step_east(self, mock_print):
        """Test arrow heading calculation when moving east"""
        self.drone.prev_pos = (4, 5)  # Previous position
        self.drone.pos = (5, 5)  # Current position
        self.drone.arrow_step()
        self.assertEqual(self.drone.heading, (1, 0))

    @patch('builtins.print')
    def test_arrow_step_west(self, mock_print):
        """Test arrow heading calculation when moving west"""
        self.drone.prev_pos = (6, 5)
        self.drone.pos = (5, 5)
        self.drone.arrow_step()
        self.assertEqual(self.drone.heading, (-1, 0))

    @patch('builtins.print')
    def test_arrow_step_north(self, mock_print):
        """Test arrow heading calculation when moving north"""
        self.drone.prev_pos = (5, 4)
        self.drone.pos = (5, 5)
        self.drone.arrow_step()
        self.assertEqual(self.drone.heading, (0, 1))

    @patch('builtins.print')
    def test_arrow_step_south(self, mock_print):
        """Test arrow heading calculation when moving south"""
        self.drone.prev_pos = (5, 6)
        self.drone.pos = (5, 5)
        self.drone.arrow_step()
        self.assertEqual(self.drone.heading, (0, -1))

    @patch('builtins.print')
    def test_check_for_crop(self, mock_print):
        """Test if drone correctly identifies mature crops"""
        # Mock a mature crop
        mock_crop = Mock(spec=CropAgent)
        mock_crop.growth_stage = "mature"
        
        # Set up the grid to return the mock crop
        self.model.grid.get_cell_list_contents.return_value = [mock_crop]
        
        self.assertTrue(self.drone.check_for_crop())
        
        # Test with immature crop
        mock_crop.growth_stage = "growing"
        self.assertFalse(self.drone.check_for_crop())

    @patch('builtins.print')
    def test_move_randomly(self, mock_print):
        """Test if move_randomly function works correctly"""
        # Mock possible steps
        possible_steps = [(4, 5), (5, 4), (6, 5), (5, 6)]
        self.model.grid.get_neighborhood.return_value = possible_steps
        chosen_position = possible_steps[0]
        self.model.random.choice.return_value = chosen_position
        
        original_pos = self.drone.pos
        self.drone.move_randomly()
        
        # Verify movement
        self.model.grid.move_agent.assert_called_with(self.drone, chosen_position)
        self.assertEqual(self.drone.prev_pos, original_pos)

    @patch('builtins.print')
    def test_return_to_base(self, mock_print):
        """Test if return_to_base moves drone toward base position"""
        self.drone.pos = (5, 5)
        self.drone.return_to_base()
        
        # Should move toward (0, 0)
        expected_position = (4, 4)  # Moving diagonally toward base
        self.model.grid.move_agent.assert_called_once()
        called_args = self.model.grid.move_agent.call_args[0]
        self.assertEqual(called_args[0], self.drone)  # First arg should be the drone
        self.assertEqual(len(called_args[1]), 2)  # Second arg should be a position tuple

    @patch('builtins.print')
    def test_step_with_crop_found(self, mock_print):
        """Test drone behavior when it finds a crop"""
        # Mock check_for_crop to return True
        with patch.object(DroneRobot, 'check_for_crop', return_value=True):
            self.drone.step()
            mock_print.assert_any_call(f"DroneRobot {self.drone.unique_id} is reporting a crop at {self.drone.pos}.")

    def test_at_base_position(self):
        """Test if drone correctly identifies when it's at base position"""
        self.drone.pos = (0, 0)  # Base position
        self.drone.return_to_base()
        self.model.grid.move_agent.assert_not_called()  # Shouldn't move if already at base

if __name__ == '__main__':
    unittest.main()
