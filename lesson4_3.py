# Переопределение Overriding

class Person:  # parent

    def __init__(self, name):
        self.name = name

    def breathe(self):
        print('Person can breathe')

    def walk(self):
        print('Person can walk')

    def sleep(self):
        print('Person is sleeping')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()



class Doctor(Person):  # subclass

    def breathe(self):
        print('Doctor can breathe')

    def __str__(self):
        return f'Doctor {self.name}'


d = Doctor('John')
p = Person('Adam')
print(p.name, d.name)  # Adam John
print(p, d)  # <__main__.Person object at 0x00000210025DA050> Doctor John
d.combo() #Doctor can breathe Person can walk Person is sleeping
