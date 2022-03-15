# magic methods for comparison
# __ eq__ - ==;     __ ne__ - !=;     __ lt__ - <;     __ le__ - <=;     __ gt__ - >;     __ ge__ - >=;
# реализовывать все 6 нет необходимости. Можно просто реализовать на равенство и больше и все остальные из них получаются
class Rectangle:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int,float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other
