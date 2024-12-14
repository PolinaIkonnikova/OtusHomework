from scr.figure import Figure


class Circle(Figure):

    pi = 3.14

    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def get_area(self) -> float:
        return self._round_result(self.pi * self.radius ** 2)

    @property
    def get_perimeter(self) -> float:
        return self._round_result(2 * self.pi * self.radius)
