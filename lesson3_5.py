# magic methods __eq__ and __hash__
# Hash определена только для неизменяемых объектов. Те когда мы определяем __eq__ hash же не получится найти
# нужно ее определить.
# Где может использоваться hash ? - ключи словаря. Если не определить ее, то не сможем экземпляры класса
# в качестве ключей подавать
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and \
               self.x == other.x and self.y == other.y

    def __hash(self):
        return hash((self.x,self.y))
