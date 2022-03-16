# Расширение extending - создание атрибута / метода, которого нет у родительского класса

class Person:
    def breathe(self):
        print("Person breathes")

    def sleep(self):
        print('Person is sleeping')

    def combo(self):
        self.sleep()
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        if hasattr(self, 'age'):
            print(self.age)


class Doctor(Person):
    age = 30

    def breathe(self):
        print("Doctor breathes")

    def sleep(self):
        print('Doctor is sleeping')

    def walk(self):
        print('Doctor walks')


p = Person()
d = Doctor()
p.combo()
print('-' * 10)
d.combo()
