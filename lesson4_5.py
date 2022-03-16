# Наследование Делегирование Delegating
# method - super()

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'

    def info(self):         # in parent class
        print('Parent class')
        print(self)         # обратится к str у доктора


class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'

    def breathe(self):
        print("Doctor breathes")
        super().breathe()  # super()  выполняет метод родительского класса


p = Person('Ivan', 'Petrov')
d = Doctor("Petr", 'Ivanov', 40)
print(p.name, p.surname)
print(d.name, d.surname, d.age)
d.info()