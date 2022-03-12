# magic methods __str__ and __repr__

class Lion:
    def __init__(self, name):
        self.name = name

    # как разработчики будут видеть этот объект класса
    def __repr__(self):
        return f'The object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name}'
