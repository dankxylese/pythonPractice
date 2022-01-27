# Pytest
from tasks_to_do.rect_square.rect_square_ex import Square, Rectangle


def test_square_perimeter():
    square = Square(3)
    assert square.get_perimeter() == 12

def test_square_area():
    square = Square(3)
    assert square.get_area() == 9

def test_rectangle_perimeter():
    rect = Rectangle(3, 4)
    assert rect.get_perimeter() == 14

def test_rectangle_area():
    rect = Rectangle(3, 4)
    assert rect.get_area() == 12

def test_squares_in_square():
    square = Square(3)
    square2 = Square(6)
    assert square.get_number_enclosing(square2) == 4

def test_squares_in_square_other_way_around():
    square = Square(6)
    square2 = Square(3)
    assert square.get_number_enclosing(square2) == 4
