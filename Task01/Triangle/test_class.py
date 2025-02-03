import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_equilateral():
    triangle = Triangle(3, 3, 3)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 9

def test_isosceles():
    triangle = Triangle(3, 3, 4)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 10

def test_nonequilateral():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12

def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)

def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 3, 3)

def test_invalid_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)