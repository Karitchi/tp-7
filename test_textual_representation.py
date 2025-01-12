import unittest
from fraction import Fraction


class TestFractionTextualRepresentation(unittest.TestCase):
    def test_str(self):
        """Test the __str__ method of the Fraction class."""
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(2, 1)), "2")
        self.assertEqual(str(Fraction(0, 1)), "0")
        self.assertEqual(str(Fraction(-3, 4)), "-3/4")
        self.assertEqual(str(Fraction(3, -4)), "-3/4")
        self.assertEqual(str(Fraction(-3, -4)), "3/4")

    def test_as_mixed_number(self):
        """Test the as_mixed_number method of the Fraction class."""
        self.assertEqual(Fraction(7, 4).as_mixed_number(), "1 3/4")
        self.assertEqual(Fraction(4, 4).as_mixed_number(), "1")
        self.assertEqual(Fraction(3, 4).as_mixed_number(), "3/4")
        self.assertEqual(Fraction(-7, 4).as_mixed_number(), "-1 3/4")
        self.assertEqual(Fraction(7, -4).as_mixed_number(), "-1 3/4")
        self.assertEqual(Fraction(-7, -4).as_mixed_number(), "1 3/4")


if __name__ == "__main__":
    unittest.main()
