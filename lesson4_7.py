# Slots
# Можно ограничить возможность создавать атрибуты
from timeit import timeit
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')  # кроме x and y нельзя другие будет создать + меньше памяти

    def __init__(self, x, y):
        self.x = x
        self.y = y

def make_cl1():
    s = Point(3,4)
    s.x = 100
    s.x
    del s.x

def make_cl2():
    s = PointSlots(3,4)
    s.x = 100
    s.x
    del s.x

s = Point(3,4)
print(s.__sizeof__(), s.__dict__.__sizeof__())
d = PointSlots(3,4)
print(d.__sizeof__())

print(timeit(make_cl1))
print(timeit(make_cl2))