from seminar_03.LSP.quad_rangle import QuadRangle


class Square(QuadRangle):
    def __init__(self, length: int):
        self.__length = length

    @property
    def length(self):
        return self.__length

    @property
    def area(self) -> int:
        return self.__length ** 2
