import unittest
from fraction import Fraction

class TestFractionPropertiesChecking(unittest.TestCase):
    def test_is_zero(self):
        """Test the is_zero method of the Fraction class."""
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 1).is_zero())
        self.assertTrue(Fraction(0, 2).is_zero())

    def test_is_integer(self):
        """Test the is_integer method of the Fraction class."""
        self.assertTrue(Fraction(2, 1).is_integer())
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(1, 2).is_integer())

    def test_is_proper(self):
        """Test the is_proper method of the Fraction class."""
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(2, 1).is_proper())
        self.assertTrue(Fraction(-1, 2).is_proper())
        self.assertFalse(Fraction(-2, 1).is_proper())

    def test_is_unit(self):
        """Test the is_unit method of the Fraction class."""
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())
        self.assertTrue(Fraction(1, 2).is_unit())

    def test_is_adjacent_to(self):
        """Test the is_adjacent_to method of the Fraction class."""
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertFalse(Fraction(1, 2).is_adjacent_to(Fraction(1, 4)))
        self.assertTrue(Fraction(2, 3).is_adjacent_to(Fraction(1, 2)))
        self.assertFalse(Fraction(2, 3).is_adjacent_to(Fraction(1, 3)))

if __name__ == "__main__":
    unittest.main()
