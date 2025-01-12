import unittest
from fraction import Fraction

class TestFractionOverloading(unittest.TestCase):
    def test_add(self):
        """Test the __add__ method of the Fraction class."""
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(1, 3) + Fraction(1, 6), Fraction(1, 2))
        self.assertEqual(Fraction(-1, 2) + Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))

    def test_sub(self):
        """Test the __sub__ method of the Fraction class."""
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(1, 3) - Fraction(1, 6), Fraction(1, 6))
        self.assertEqual(Fraction(-1, 2) - Fraction(1, 2), Fraction(-1, 1))
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))

    def test_mul(self):
        """Test the __mul__ method of the Fraction class."""
        self.assertEqual(Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4))
        self.assertEqual(Fraction(1, 3) * Fraction(1, 6), Fraction(1, 18))
        self.assertEqual(Fraction(-1, 2) * Fraction(1, 2), Fraction(-1, 4))
        self.assertEqual(Fraction(1, 2) * Fraction(1, 3), Fraction(1, 6))

    def test_truediv(self):
        """Test the __truediv__ method of the Fraction class."""
        self.assertEqual(Fraction(1, 2) / Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(1, 3) / Fraction(1, 6), Fraction(2, 1))
        self.assertEqual(Fraction(-1, 2) / Fraction(1, 2), Fraction(-1, 1))
        self.assertEqual(Fraction(1, 2) / Fraction(1, 3), Fraction(3, 2))

    def test_pow(self):
        """Test the __pow__ method of the Fraction class."""
        self.assertEqual(Fraction(1, 2) ** 2, Fraction(1, 4))
        self.assertEqual(Fraction(2, 3) ** 3, Fraction(8, 27))
        self.assertEqual(Fraction(-1, 2) ** 2, Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) ** -1, Fraction(2, 1))

    def test_eq(self):
        """Test the __eq__ method of the Fraction class."""
        self.assertTrue(Fraction(1, 2) == Fraction(1, 2))
        self.assertTrue(Fraction(2, 4) == Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) == Fraction(1, 3))
        self.assertTrue(Fraction(-1, 2) == Fraction(1, -2))

    def test_float(self):
        """Test the __float__ method of the Fraction class."""
        self.assertAlmostEqual(float(Fraction(1, 2)), 0.5)
        self.assertAlmostEqual(float(Fraction(1, 3)), 1/3)
        self.assertAlmostEqual(float(Fraction(-1, 2)), -0.5)
        self.assertAlmostEqual(float(Fraction(2, 1)), 2.0)
        self.assertAlmostEqual(float(Fraction(0, 1)), 0.0)

if __name__ == "__main__":
    unittest.main()
