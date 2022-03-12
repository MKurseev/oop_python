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

class Vector:

    def __init__(self, *args):
        self.values = [str(i) for i in args if isinstance(i, int)]
        self.values.sort()

    def __str__(self):
        return f"Вектор({', '.join(self.values)})" if len(self.values) != 0 \
            else f'Пустой вектор'

# ____________________________________________________________________________________________
# 3.3
