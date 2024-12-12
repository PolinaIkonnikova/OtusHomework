from typing import Any


class Figure:

    def __init__(self, first_param: float, second_param: float = None) -> None:
        self.first_param = first_param
        self.second_param = second_param

    @property
    def get_area(self) -> float:
        return self.first_param * self.second_param

    @property
    def get_perimeter(self) -> float:
        return 2 * (self.first_param + self.second_param)

    def add_area(self, figure: Any) -> float:
        if not isinstance(figure, Figure):
            raise ValueError(f"{figure} is not a Figure object")
        return self.get_area + figure.get_area
