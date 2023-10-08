from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area == area
    assert r.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, 24, -20),
                          (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        return Rectangle(side_a, side_b)


@pytest.mark.parametrize(("side_square", "area", "perimeter"),
                         [(5, 25, 20)])
def test_square(side_square, area, perimeter):
    s = Square(side_square)
    assert s.name == f"Square {side_square}"
    assert s.get_area == area
    assert s.get_perimeter == perimeter


@pytest.mark.parametrize(("side_square", "area", "perimeter"),
                         [(-5, 25, -20),
                          (0, 0, 0)])
def test_square_negative(side_square, area, perimeter):
    with pytest.raises(ValueError):
        return Square(side_square)


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(4, 5, 6, 9.92, 15)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert t.get_area == area
    assert t.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(-4, -5, -6, 49.22, -15),
                          (0, 0, 0, 0, 0)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        return Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(5, 78.54, 31.42)])
def test_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == f"Circle {radius}"
    assert c.get_area == area
    assert c.get_perimeter == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-5, 78.54, -31.42),
                          (0, 0, 0)])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        return Circle(radius)


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    c = Circle(5)
    t = Triangle(4, 5, 6)
    assert r.add_area(s) == 35
    assert t.add_area(c) == 88
    assert c.add_area(r) == 89
    assert s.add_area(t) == 35


def test_add_area_negative():
    with pytest.raises(ValueError):
        r = Rectangle(-2, 5)
        s = Square(-4)
        t = Triangle(-4, 5, 6)
        c = Circle(-5)
        assert r.add_area(s) == 35
        assert t.add_area(c) == 88
        assert c.add_area(r) == 129
        assert s.add_area(c) == 41
