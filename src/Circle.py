from math import pi
from src.FIgure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create Circle, check value")
        self.name = f"Circle {radius}"
        self.radius = radius

    @property
    def get_area(self):
        return round(pi * (self.radius ** 2), 2)

    @property
    def get_perimeter(self):
        return round(2 * pi * self.radius, 2)


c = Circle(5)
c.get_area
c.get_perimeter
