# ____________________________________________________________________________________________
# 4.1

class Vehicle:
    pass


class Car(Vehicle):
    pass


class Boat(Vehicle):
    pass


class Plane(Vehicle):
    pass


class RaceCar(Car):
    pass

# ____________________________________________________________________________________________
# 4.2

class NewInt(int):

    def repeat(self,n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(format(self, '10b'))

# ____________________________________________________________________________________________
# 4.5 task 1
