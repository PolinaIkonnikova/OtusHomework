from abc import abstractmethod, ABC


class Figure(ABC):

    @abstractmethod
    @property
    def get_area(self) -> float:
        ...

    @abstractmethod
    @property
    def get_perimeter(self) -> float:
        ...

    def add_area(self, figure: 'Figure') -> float:
        if not isinstance(figure, Figure):
            raise ValueError(f"{figure} is not a Figure object")
        return self.get_area + figure.get_area
