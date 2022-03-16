# Множественное наследование

class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Grats, i became a doctor')

    def can_cure(self):
        print('I am a doctor, i can heal')

    def can_build(self):
        print('I am a doctor, i can build but worse')

class Builder:

    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Grats, i became a Builder')

    def can_build(self):
        print('I am a builder, i can build')

class Person(Doctor, Builder):

    def __init__(self, rank, degree):
        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f'Person {self.rank} {self.degree}'

    def graduate(self):
        print('look how i became')
        super().graduate()
        Builder.graduate(self)

p = Person(5, 'spec')
print(p)
print(Person.__mro__) # (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)
p.can_build() # I am a doctor, i can build but worse. Because class Doctor first
p.graduate()
