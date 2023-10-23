from seminar_03.LSP.quad_rangle import QuadRangle


class Rectangle(QuadRangle):
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    @property
    def area(self) -> int:
        return self.height * self.width
