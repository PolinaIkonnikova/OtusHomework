from abc import abstractmethod, ABC


class Figure(ABC):

    round_count: int = 2

    @classmethod
    def set_round_count(cls, num: int):
        cls.round_count = num

    @property
    @abstractmethod
    def get_area(self) -> float:
        ...

    @property
    @abstractmethod
    def get_perimeter(self) -> float:
        ...

    def _round_result(self, result: float) -> float:
        return round(result, self.round_count)

    def add_area(self, figure: 'Figure') -> float:
        if not isinstance(figure, Figure):
            raise ValueError(f"{figure} is not a Figure object")
        return self._round_result(self.get_area + figure.get_area)
