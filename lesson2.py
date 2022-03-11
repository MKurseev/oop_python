# вычисляемые property
# мы пришли к тому, что сделали и side и area атрибутами настраиваемыми, вместо того
# чтобы это была функция просто
class Square:

    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side ** 2
        return self.__area
#_____________________________________________________________________

# classmethod and staticmethod

# Проблема : функцию hello мы не можем вызвать элементом класса, но можем классом
# а функцию instance_hello не можем вызвать классом, но можем экземпляром класса
class Example:
    def hello():
        print('Hello')

    def instance_hello(self):
        print(f'Hello {self}')

    @staticmethod   # не привязывается ни к экземпляру, ни к классу
    def static_hello():
        print('static hello')

    # нужен, когда хотим сделать обработку не над экземпляром,
    # а над классом
    # Внутри cls нам уже доступен класс со всеми методами и атрибутами
    @classmethod
    def class_hello(cls):
        print(f'Hello {cls}')
#_____________________________________________________________________

# 2.9 from stepic
class Robot:
    population = 0

    def __init__(self,name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population += 1

    def destroy(self):
        print(f'Робот {self.name} был уничтожен')
        Robot.population -= 1

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')

r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"
#_____________________________________________________________________

