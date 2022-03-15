# magic methods __add__ - сложение , __mul__ - умножение , __sub__ - вычитание , __truediv__ - деление

class BankAccount:
    def __init__(self, name, balance):
        print('new object init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    # прикол в том, что self стоит слева, а этот метод справа проверяет нахождение объекта
    def __radd__(self, other):
        print('__radd__ call')
        return self + other

    def __mul__(self, other):
        print('__add__ call')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance * other)  # прост усложнили чтоб задача интереснее была. sugar
        if isinstance(other, str):
            return self.name + other  # joke
        raise NotImplemented
