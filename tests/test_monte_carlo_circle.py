import unittest
import random

from monte_carlo.monte_carlo_circle import monte_carlo_circle_area

class TestMonteCarloCircleArea(unittest.TestCase):
    def test_num_points_positive(self):
        random.seed(0)
        area = monte_carlo_circle_area(1, num_points=1000)
        self.assertGreater(area, 2.9)
        self.assertLess(area, 3.4)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            monte_carlo_circle_area(-1, 1000)
        with self.assertRaises(ValueError):
            monte_carlo_circle_area(1, 0)

if __name__ == '__main__':
    unittest.main()
