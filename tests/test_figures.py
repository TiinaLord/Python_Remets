from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20),
                          (5, 10, 50, 30)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, 24, -20),
                          (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_square", "area", "perimeter"),
                         [(5, 25, 20),
                          (10, 100, 40)])
def test_square(side_square, area, perimeter):
    r = Square(side_square)
    assert r.name == f"Square {side_square}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_square", "area", "perimeter"),
                         [(-5, 25, -20),
                          (0, 0, 0)])
def test_square_negative(side_square, area, perimeter):
    with pytest.raises(ValueError):
        s = Square(side_square)
        assert s.name == f"Square {side_square}"
        assert s.get_area() == area
        assert s.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(4, 5, 6, 9.92, 15),
                          (10, 10, 10, 43.30, 30)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(-4, -5, -6, 49.22, -15),
                          (0, 0, 0, 0, 0)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
        assert t.name == f"Triangle {side_a} and {side_b} and {side_c}"
        assert t.get_area() == area
        assert t.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(5, 78.54, 31.42),
                          (10, 314.16, 62.83)])
def test_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == f"Circle {radius}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-5, 78.54, -31.42),
                          (0, 0, 0)])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert c.name == f"Circle {radius}"
        assert c.get_area() == area
        assert c.get_perimeter() == perimeter


def test_add_area_rectangle_square():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 35


def test_add_area_triangle_circle():
    t = Triangle(4, 5, 6)
    c = Circle(5)
    assert t.add_area(c) == 88


def test_add_area_square_square():
    s1 = Square(4)
    s2 = Square(5)
    assert s1.add_area(s2) == 41


def test_add_area_circle_rectangle():
    c = Circle(5)
    r = Rectangle(10, 5)
    assert c.add_area(r) == 129


def test_add_area_negative_rectangle_square():
    with pytest.raises(ValueError):
        r = Rectangle(2, 5)
        s = Square(-4)
        assert r.add_area(s) == 35


def test_add_area_negative_triangle_circle():
    with pytest.raises(ValueError):
        t = Triangle(-4, 5, 6)
        c = Circle(5)
        assert t.add_area(c) == 88


def test_add_area_negative_square_square():
    with pytest.raises(ValueError):
        s1 = Square(-4)
        s2 = Square(5)
        assert s1.add_area(s2) == 41


def test_add_area_negative_circle_rectangle():
    with pytest.raises(ValueError):
        c = Circle(-5)
        r = Rectangle(-10, -5)
        assert c.add_area(r) == 129
