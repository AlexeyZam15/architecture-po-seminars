from seminar_03.LSP.quad_rangle import QuadRangle
from seminar_03.LSP.rectangle import Rectangle
from seminar_03.LSP.square import Square

t1: QuadRangle = Rectangle(4, 5)
t2: QuadRangle = Square(4)
print(f"{t1.area = }, {t2.area = }")
