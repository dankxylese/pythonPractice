from lesson_unit_testing.simplecalc import SimpleCalc
import unittest


# Class that inherits from TestCase (class in unittest)

# Unit Tests

class CalcTests(unittest.TestCase):
    def setUp(self):  # setup for things we need to use on every test separately, in case things in setup hold data
        # in memory
        self.calc = SimpleCalc()
        print("Setting up")

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(5, 2)
        expected = 3
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multiply(2, 4)
        expected = 8
        print(actual, expected)
        self.assertEqual(actual, expected)

    def test_divide(self):
        actual = self.calc.divide(8, 4)
        expected = 2
        self.assertEqual(actual, expected)