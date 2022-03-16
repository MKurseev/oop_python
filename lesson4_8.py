class Rectangle:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value


class Square(Rectangle):
    pass

class Square2(Rectangle):
    __slots__ = 'color'  # Slots дочернего класса расширяет slots Родительского
    def __init__(self, a, b, color):
        super().__init__(a,b)
        self.color = color


c = Rectangle(5, 6)
print(c.width)

s = Square(4, 5)
print(s.__dict__)  # у родительского класса не будет dict из-за slots, а у subclass будет

d = Square2(4,4,'red')
print(d.color, d.width, d.height)  # тут dict снова нет.