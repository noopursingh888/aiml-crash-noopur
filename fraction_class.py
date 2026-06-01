# This program demonstrates dunder (magic) methods
# using a custom Fraction class


import math


class Fraction:

    def __init__(self, numerator, denominator):

        self.numerator = numerator
        self.denominator = denominator


    def simplify(self):

        gcd = math.gcd(self.numerator, self.denominator)

        return Fraction(
            self.numerator // gcd,
            self.denominator // gcd
        )


    def __str__(self):

        return f"{self.numerator}/{self.denominator}"


    def __add__(self, other):

        new_numerator = (
            self.numerator * other.denominator +
            other.numerator * self.denominator
        )

        new_denominator = (
            self.denominator * other.denominator
        )

        result = Fraction(new_numerator, new_denominator)

        return result.simplify()


    def __eq__(self, other):

        first = self.simplify()

        second = other.simplify()

        return (
            first.numerator == second.numerator and
            first.denominator == second.denominator
        )


    def __lt__(self, other):

        return (
            self.numerator * other.denominator <
            other.numerator * self.denominator
        )



f1 = Fraction(1, 2)

f2 = Fraction(1, 4)

f3 = Fraction(2, 4)

f4 = Fraction(3, 5)

f5 = Fraction(4, 10)


print("Fraction 1:", f1)

print("Fraction 2:", f2)


print("\nAddition:")

print(f"{f1} + {f2} = {f1 + f2}")


print("\nEquality Check:")

print(f"{f1} == {f3} :", f1 == f3)

print(f"{f4} == {f5} :", f4 == f5)


print("\nLess Than Comparison:")

print(f"{f2} < {f1} :", f2 < f1)

print(f"{f4} < {f1} :", f4 < f1)


# @functools.total_ordering automatically creates
# remaining comparison methods if we define __eq__
# and one comparison method like __lt__.