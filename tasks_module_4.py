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

    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(format(self, '10b'))


# ____________________________________________________________________________________________
# 4.5 task 1

class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')


class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


# ____________________________________________________________________________________________
# 4.5 task 2

class Initialization:

    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print('Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    @staticmethod
    def check(fun, first, other):
        if isinstance(other, (int, Vegetarian, MeatEater)):
            if hasattr(other, "capacity"):
                return fun(first, other.capacity)
            return fun(first, other)
        return f"Невозможно сравнить количество сладкоежек с {other}"

    def __eq__(self, other):
        return self.check(lambda x, y: x == y, self.capacity, other)

    def __lt__(self, other):
        return self.check(lambda x, y: x < y, self.capacity, other)

    def __gt__(self, other):
        return self.check(lambda x, y: x > y, self.capacity, other)


# ____________________________________________________________________________________________
# 5.1

class Wallet:

    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        if len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        if not currency.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        if self.currency != other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == other.balance

    def __add__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance + other.balance)
        else:
            raise ValueError("Данная операция запрещена")

    def __sub__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance - other.balance)
        else:
            raise ValueError("Данная операция запрещена")