# magic method __call__
# () - это оператор вызова. Класс - вызываемый объект. Экземпляр - нет

# Где применяется :
# 1. Избавление от замыкания
class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Наш экземпляр вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length


# 2. В качестве декоратора
from time import perf_counter


class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()

        print(f'Вызывается ф-ция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)

        finish = perf_counter()
        print(f'Ф-я отработала за {finish - start}')
        return result


def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fact(7))

# тут уже повесили декоратор
fact = Timer(fact)
print(fact(7))
# декоратор на функцию фибоначи
print(Timer(fib)(20))
