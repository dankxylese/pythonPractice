"""
Using TDD and unit tests
Define rectangle and square classes
One should inherit from the other

Rectangle - defined with length and width
Square - defined with just side length

Methods:
- get_perimeter
- get_area

Square method:
- get_number_enclosing
takes another square as an argument, and returns
the number of that square that would fit inside
the current square

Both classes should have appropriate repr and str
"""

import math


class Square:
    def __init__(self, side):
        self.side = side

    def __repr__(self):
        return f"side: {self.side}"

    def __str__(self):
        return f"Side of the square is: {self.side}"

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2

    def get_number_enclosing(self, square):
        if self.side >= square.side:
            return int(math.floor(self.side / square.side))
        else:
            return 0


class Rectangle(Square):
    def __init__(self, side1, side2):
        super().__init__(side1)
        self.side2 = side2

    def __repr__(self):
        return f"width: {self.side} \nlength: {self.side2}"

    def __str__(self):
        return f"Width of the rectangle is: {self.side} \nLength of the rectangle is: {self.side2}"

    def get_perimeter(self):
        print(self.side)
        return (self.side * 2) + (self.side2 * 2)

    def get_area(self):
        return self.side * self.side2

    def get_number_enclosing(self, square):
        return None
