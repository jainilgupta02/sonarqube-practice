import unittest
from app import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -3), 2)
    
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 4), 6)
    
    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -4), -6)
    
    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(5, 10), -5)
    
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(4, 5), 20)
    
    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-4, -5), 20)
    
    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(4, -5), -20)
    
    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)
    
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)
    
    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(10, -2), -5)
    
    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), "Error: Cannot divide by zero")
    
    def test_divide_with_float_result(self):
        self.assertEqual(divide(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()
