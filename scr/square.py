from scr.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, param: float) -> None:
        super().__init__(param, param)
