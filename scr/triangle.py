from math import sqrt
from scr.figure import Figure


class Triangle(Figure):

    def __init__(self, first_param: float, second_param: float, third_param: float) -> None:
        super().__init__(first_param, second_param)
        self.third_param = third_param
        if not self._is_valid_triangle():
            raise ValueError("You must back to the school and learn geometry. "
                             "You can't create the triangle with these params.")

    def _is_valid_triangle(self) -> bool:
        sort_sides = sorted([self.first_param, self.second_param, self.third_param])
        return sort_sides[0] + sort_sides[1] > sort_sides[2]

    def get_area(self) -> float:
        half_per = self.get_perimeter() / 2
        return sqrt(half_per * (half_per - self.first_param) * (half_per - self.second_param) *
                    (half_per - self.third_param))

    def get_perimeter(self) -> float:
        return self.first_param + self.second_param + self.third_param
