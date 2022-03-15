# 3.1 task 1
class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender not in ['male', 'female']:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        return f'Гражданин {self.surname} {self.name}' if self.gender == 'male' \
            else f'Гражданка {self.surname} {self.name}'


# ____________________________________________________________________________________________
# 3.1 task 2

class Vector2:

    def __init__(self, *args):
        self.values = [str(i) for i in args if isinstance(i, int)]
        self.values.sort()

    def __str__(self):
        return f"Вектор({', '.join(self.values)})" if len(self.values) != 0 \
            else f'Пустой вектор'


# ____________________________________________________________________________________________
# 3.3

class Vector:

    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        return f"Вектор{tuple(self.values)}" if len(self.values) != 0 \
            else f'Пустой вектор'

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*(i + other for i in self.values))
        elif isinstance(other, Vector):
            if len(other) != len(self.values):
                return print('Сложение векторов разной длины недопустимо')
            else:
                return Vector(*(other.values[i] + self.values[i] for i in range(len(other))))
        else:
            return print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*(i * other for i in self.values))
        elif isinstance(other, Vector):
            if len(other) != len(self.values):
                return print('Умножение векторов разной длины недопустимо')
            else:
                return Vector(*(other.values[i] * self.values[i] for i in range(len(other))))
        else:
            return print(f'Вектор нельзя умножать с {other}')


# ____________________________________________________________________________________________
# 3.4

class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return 'Невозможно выполнить сравнение'


# ____________________________________________________________________________________________
# 3.6 task 1

class City:

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in ('a', 'e', 'i', 'o', 'u')


# ____________________________________________________________________________________________
# 3.6 task 2

class Quadrilateral:

    def __init__(self, width, height=None):
        self.height = height or width
        self.width = width

    def __str__(self):
        return f'Куб размером {self.width}x{self.height}' if self.width == self.height else f'Прямоугольник размером {self.width}x{self.height}'

    def __bool__(self):
        return self.height == self.width
