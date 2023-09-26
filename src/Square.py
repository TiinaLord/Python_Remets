from src.FIgure import Figure


class Square(Figure):
    def __init__(self, side_square):
        super().__init__()
        if side_square <= 0:
            raise ValueError("Can't create Square, check value")
        self.name = f"Square {side_square}"
        self.side_square = side_square

    @property
    def get_area(self):
        return self.side_square * self.side_square

    @property
    def get_perimeter(self):
        return 2 * (self.side_square + self.side_square)


s = Square(5)
s.get_area
s.get_perimeter
