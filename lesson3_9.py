# magic methods __getitem__ , __setitem__, __delitem__

class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError('Index is out of our collection')

    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):
            self.values[key - 1] = value
        elif key > len(self.values):  # возможность создавать разряженный список
            diff = key - len(self.values)
            self.values.extend([0] * diff)
            self.values[key - 1] = value
        else:
            raise IndexError("Index is out of our collection")

    def __delitem__(self, key):
        if 0 < key <= len(self.values):
            del self.values[key - 1]
        else:
            raise IndexError("Index is out of our collection")


v3 = Vector(12, 4, 6, 23, 1, 5, 7, 41)
print(v3[1])
v5 = Vector(124, 65, 2, 66, 2)
print(v5)
v5[2] = 100
print(v5)
del v5[2]
print(v5)

v5[9] = 4
print(v5)
