# magic method __bool__
# bool - ненулевое / непустое значение или нулевое/пустое ( если bool не определена, питон лезет в len)
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x != 0 or self.y != 0


