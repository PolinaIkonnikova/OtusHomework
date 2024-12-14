import pytest
from scr.circle import Circle
from scr.figure import Figure
from scr.rectangle import Rectangle
from scr.square import Square
from scr.triangle import Triangle


@pytest.mark.parametrize("figure_obj, right_area, right_perimeter", [
    (Circle(3), 28.26, 18.84),
    (Rectangle(3, 4), 12, 14),
    (Square(3), 9, 12),
    (Triangle(3, 4, 5), 6, 12)
    ]
)
def test_get_area(figure_obj: Figure, right_area: float | int, right_perimeter: float | int):
    assert figure_obj.get_area == right_area
    assert figure_obj.get_perimeter == right_perimeter


def test_create_wrong_triangle():
    with pytest.raises(ValueError):
        _ = Triangle(1, 2, 10)


@pytest.mark.parametrize("first_fig, second_fig, right_area", [
    (Circle(3), Rectangle(3, 4), 40.26),
    (Square(3), Triangle(3, 4, 5), 15),
    ]
)
def test_add_area(first_fig: Figure, second_fig: Figure, right_area: float):
    assert first_fig.add_area(second_fig) == right_area


def test_add_area_no_figure():
    with pytest.raises(ValueError):
        _ = Circle(3).add_area(23)
