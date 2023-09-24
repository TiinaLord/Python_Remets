from src.FIgure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle, check values")
        self.name = f"Triangle {side_a} and {side_b} and {side_c}"
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        semi_p = (self.side_a + self.side_b + self.side_c) / 2
        return round((semi_p * (semi_p - self.side_a) * (semi_p - self.side_b) * (semi_p - self.side_c)) ** 0.5, 2)

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
