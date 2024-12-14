from scr.figure import Figure


class Rectangle(Figure):

    def __init__(self, first_param: float, second_param: float) -> None:
        self.first_param = first_param
        self.second_param = second_param

    @property
    def get_area(self) -> float:
        return self.first_param * self.second_param

    @property
    def get_perimeter(self) -> float:
        return 2 * (self.first_param + self.second_param)
