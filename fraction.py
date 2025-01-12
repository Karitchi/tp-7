class Fraction:
    """Class representing a fraction and operations on it

    Author: V. Van den Schrieck
    Date: October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """
        Initializes a fraction with a numerator and a denominator.

        PRE:
            - `num` and `den` are integers.
            - `den` != 0 (denominator cannot be zero).
        POST:
            - A fraction is created in its reduced form.
        RAISES:
            - `ValueError` if `den` is zero.
            - `TypeError` if `num` or `den` is not an integer.

        """

        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Both numerator and denominator must be integers.")

        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        if den < 0:
            num = -num
            den = -den

        self.num = num
        self.den = den
        self._reduce()

    @property
    def numerator(self) -> int:
        """Gets the numerator of the fraction.

        PRE:
            - None.
        POST:
            - Returns the numerator of the fraction.
        """
        return self.num

    @property
    def denominator(self) -> int:
        """Gets the denominator of the fraction.

        PRE:
            - None.
        POST:
            - Returns the denominator of the fraction.
        """
        return self.den

    def _reduce(self):
        """Reduces the fraction to its simplest form.

        PRE:
            - None.
        POST:
            - The fraction is in its simplest form.
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        gcd_value = gcd(self.num, self.den)
        self.num //= gcd_value
        self.den //= gcd_value

    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Returns a textual representation of the fraction in reduced form.

        PRE:
            - None.
        POST:
            - Returns a string representation of the fraction.
        """
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

    def as_mixed_number(self) -> str:
        """Returns a textual representation of the fraction as a mixed number.

        A mixed number is the sum of an integer and a proper fraction.

        PRE:
            - None.
        POST:
            - Returns a string representation of the fraction as a mixed number.
        """
        integer_part = abs(self.num) // self.den
        remainder = abs(self.num) % self.den
        sign = "-" if self.num < 0 else ""
        if remainder == 0:
            return f"{sign}{integer_part}"
        elif integer_part == 0:
            return f"{sign}{remainder}/{self.den}"
        return f"{sign}{integer_part} {remainder}/{self.den}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other: "Fraction") -> "Fraction":
        """Overloads the + operator for fraction addition.

        PRE:
            - `other` is an instance of `Fraction`.
        POST:
            - Returns a new `Fraction` representing the sum of the fractions.
        RAISES:
            - `TypeError` if `other` is not an instance of `Fraction`.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Overloads the - operator for fraction subtraction.

        PRE:
            - `other` is an instance of `Fraction`.
        POST:
            - Returns a new `Fraction` representing the difference of the fractions.
        RAISES:
            - `TypeError` if `other` is not an instance of `Fraction`.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Overloads the * operator for fraction multiplication.

        PRE:
            - `other` is an instance of `Fraction`.
        POST:
            - Returns a new `Fraction` representing the product of the fractions.
        RAISES:
            - `TypeError` if `other` is not an instance of `Fraction`.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Overloads the / operator for fraction division.

        PRE:
            - `other` is an instance of `Fraction`.
            - `other.num` != 0 (division by zero is not allowed).
        POST:
            - Returns a new `Fraction` representing the division of the fractions.
        RAISES:
            - `TypeError` if `other` is not an instance of `Fraction`.
            - `ZeroDivisionError` if `other.num` is zero.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator 0.")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __pow__(self, power: int) -> "Fraction":
        """Overloads the ** operator for fraction exponentiation.

        PRE:
            - `power` is an integer.
        POST:
            - Returns a new `Fraction` where both numerator and denominator are raised to the power.
        """
        if power < 0:
            return Fraction(self.den**-power, self.num**-power)
        return Fraction(self.num**power, self.den**power)

    def __eq__(self, other: "Fraction") -> bool:
        """Overloads the == operator to compare two fractions.

        PRE:
            - `other` is an instance of `Fraction`.
        POST:
            - Returns `True` if the two fractions are equal, otherwise `False`.
        RAISES:
            - `TypeError` if `other` is not an instance of `Fraction`.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        return self.num * other.den == self.den * other.num

    def __float__(self) -> float:
        """Returns the decimal value of the fraction.

        PRE:
            - None.
        POST:
            - Returns the fraction as a float.
        """
        return self.num / self.den

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Checks if the fraction's value is zero.

        PRE:
            - None.
        POST:
            - Returns `True` if the fraction is zero, otherwise `False`.
        """
        return self.num == 0

    def is_integer(self) -> bool:
        """Checks if the fraction is an integer.

        PRE:
            - None.
        POST:
            - Returns `True` if the fraction is an integer, otherwise `False`.
        """
        return self.num % self.den == 0

    def is_proper(self) -> bool:
        """Checks if the absolute value of the fraction is less than 1.

        PRE:
            - None.
        POST:
            - Returns `True` if the fraction is proper, otherwise `False`.
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self) -> bool:
        """Checks if the fraction's numerator is 1 in its reduced form.

        PRE:
            - None.
        POST:
            - Returns `True` if the numerator is 1 and the denominator is greater than 1, otherwise `False`.
        """
        return self.num == 1 and self.den > 1

    def is_adjacent_to(self, other: "Fraction") -> bool:
        """Checks if two fractions differ by a unit fraction.

        Two fractions are adjacent if the absolute value of the difference is a unit fraction.

        PRE:
            - `other` is an instance of `Fraction`.
        POST:
            - Returns `True` if the two fractions are adjacent, otherwise `False`.
        RAISES:
            - `TypeError` if `other` is not an instance of `Fraction`.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction.")
        diff = self - other
        return abs(diff.num) == 1 and diff.den == abs(self.den * other.den)
