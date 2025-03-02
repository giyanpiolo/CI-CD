import unittest
import calculator

class TestCalculator(unittest.TestCase):

  def test_add(self):
    self.assertEqual(calculator.add(5, 3), 8)
    self.assertEqual(calculator.add(-1, 1), 0)
    self.assertEqual(calculator.add(-1, -1), -2)

  def test_subtract(self):
    self.assertEqual(calculator.subtract(10, 4), 6)
    self.assertEqual(calculator.subtract(1, 5), -4)
    self.assertEqual(calculator.subtract(-1, -1), 0)

  def test_multiply(self):
    self.assertEqual(calculator.multiply(6, 7), 42)
    self.assertEqual(calculator.multiply(-2, 3), -6)
    self.assertEqual(calculator.multiply(-2, -3), 6)
    self.assertEqual(calculator.multiply(0, 5), 0)

  def test_divide(self):
    self.assertEqual(calculator.divide(8, 2), 4)
    self.assertEqual(calculator.divide(10, 5), 2)
    self.assertEqual(calculator.divide(-10, 2), -5)
    self.assertEqual(calculator.divide(10, -2), -5)

  def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
      calculator.divide(8, 0)

if __name__ == '__main__':
  unittest.main()