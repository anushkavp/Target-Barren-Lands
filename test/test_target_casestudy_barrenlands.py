import unittest

# Import the functions to be tested
from target_casestudy_barrenlands import parse_input, create_grid, mark_barren_lands, find_fertile_land

class TestBarrenLandAnalysis(unittest.TestCase):

    def test_parse_input(self):
        input_data = '{"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}'
        expected_output = [(48, 192, 351, 207), (48, 392, 351, 407), (120, 52, 135, 547), (260, 52, 275, 547)]
        self.assertEqual(parse_input(input_data), expected_output)

    def test_create_grid(self):
        m, n = 4, 5  
        grid = create_grid(m, n)
        expected_output = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        self.assertEqual(grid, expected_output)

    def test_mark_barren_lands(self):
        m, n = 5, 5
        grid = create_grid(m, n)
        barren_land_coords = [(1, 1, 2, 2)]
        expected_grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        marked_grid = mark_barren_lands(grid, barren_land_coords)
        self.assertEqual(marked_grid, expected_grid)

    def test_find_fertile_land(self):
        m, n = 5, 5
        grid = create_grid(m, n)
        barren_land_coords = '{"1 1 2 2"}'
        barren_land_coords = parse_input(barren_land_coords)
        marked_grid = mark_barren_lands(grid, barren_land_coords)
        expected_fertile_areas = [21]  # grid minus the 4 barren cells
        fertile_areas = find_fertile_land(marked_grid, 5,5)
        self.assertEqual(fertile_areas, expected_fertile_areas)

    def test_full_integration(self):
        input_data = '{"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}'
        barren_land_coords = parse_input(input_data)
        m=400
        n=600
        grid = create_grid(m, n)
        mark_barren_lands(grid, barren_land_coords)
        expected_fertile_areas = [22816, 192608] 
        fertile_areas = find_fertile_land(grid, m, n)
        self.assertEqual(fertile_areas, expected_fertile_areas)

if __name__ == '__main__':
    unittest.main()