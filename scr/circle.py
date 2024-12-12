from scr.figure import Figure


class Circle(Figure):

    pi = 3.14

    def __init__(self, radius: float) -> None:
        super().__init__(first_param=radius)

    @property
    def get_area(self) -> float:
        return self.pi * self.first_param ** 2

    @property
    def get_perimeter(self) -> float:
        return 2 * self.pi * self.first_param
