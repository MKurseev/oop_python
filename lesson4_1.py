# Наследование

# person - базовый класс - parent class
# doctor and architect - подклассы родительского класса - subclass

class Person:  # Parent

    def can_breathe(self):
        print('can breathe')

    def can_walk(self):
        print('can walk')


class Doctor(Person):  # subclass

    def can_cure(self):
        print('can cure')


class Architect(Person):  # subclass

    def can_build(self):
        print('can build')

class Ortoped(Doctor):
    pass


d = Doctor()
a = Architect()
e = Ortoped()
e.can_walk()
e.can_breathe()
print(issubclass(Doctor, Person))
print(issubclass(Person, Doctor))
print(isinstance(d, Doctor))
print(isinstance(d, Person))
