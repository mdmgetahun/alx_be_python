import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, 5), -4)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 6), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
    def test_division(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(7, 0), None)

if __name__ == '__main__':
    unittest.main()

    
