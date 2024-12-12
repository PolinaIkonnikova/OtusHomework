from scr.figure import Figure


class Square(Figure):

    def __init__(self, param: float) -> None:
        super().__init__(param, param)
