# magic methods __iter__, __next__
# нужны для того, чтобы можно было в цикле проходить экземпляры. Те сделать класс итерабельным ( iterable)

class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    # 1. Через __getitem__
    def __getitem__(self, item):
        return self.marks[item]

    # 2. Метод __iter__
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.surname):
            raise StopIteration
        letter = self.surname[self.index]
        self.index += 1
        return letter


igor = Student('Igor', 'Nikolaev', [3, 4, 5, 6, 3])
for i in igor:  # iter сильнее getitem
    print(i)


# -----------------
class Mark:

    def __init__(self, values):
        self.value = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call next marks')
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print('call next students')
        if self.index >= len(self.surname):
            raise StopIteration
        letter = self.surname[self.index]
        self.index += 1
        return letter


m = Mark([3, 4, 6, 2, 4, 2])

igor = Student('Igor', 'Nikolaev', m)
for i in igor:  # iter сильнее getitem
    print(i)
