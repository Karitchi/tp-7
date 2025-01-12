import unittest
from fraction import Fraction

class TestFractionInitialization(unittest.TestCase):
    def test_default_initialization(self):
        """Test default initialization (no arguments)."""
        fraction = Fraction()
        self.assertEqual(fraction.numerator, 0)
        self.assertEqual(fraction.denominator, 1)

    def test_valid_initialization(self):
        """Test initialization with valid numerator and denominator."""
        fraction = Fraction(3, 4)
        self.assertEqual(fraction.numerator, 3)
        self.assertEqual(fraction.denominator, 4)

    def test_invalid_denominator_zero(self):
        """Test that a zero denominator raises a ValueError."""
        with self.assertRaises(ValueError):
            Fraction(3, 0)

    def test_invalid_types(self):
        """Test that non-integer types raise a TypeError."""
        with self.assertRaises(TypeError):
            Fraction(3.5, 2)

        with self.assertRaises(TypeError):
            Fraction(3, "2")
