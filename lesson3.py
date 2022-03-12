# Пространство имен класса

class DepartmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    # как обращаться к переменным класса.
    # 1 способ - через self
    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    #  2 способ - через сам класс
    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    #  3 способ - через property (getter), это уже свойство, а не метод (функция)
    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    #  4 способ - через classmethod  ( на вход сам класс)
    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    #  5 способ - через staticmethod  ( на вход ничего не принимается)
    @staticmethod
    def info_stat():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)


# _____________________________________________________________________
# Practice time  ( all topics covered above)
from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'sdfsafgsdcvb'

    @property
    def secret(self):
        s = input('Password: ')
        if s == self.password:
            print(self.__secret)
        else:
            raise ValueError('Wrong password')

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, new_password):
        print('setter called')
        if not isinstance(new_password, str):
            raise TypeError("Password mast be a string")
        if len(new_password) < 4:
            raise ValueError('Password is too short, 4 is the minimum length')
        if len(new_password) > 12:
            raise ValueError('Password is too long, 12 is the maximum length')
        if not User.is_include_number(new_password):
            raise ValueError('Password should include at least one number')
        self.__password = new_password


# x = User('aaa', '123rtgr')
# x.secret


# _____________________________________________________________________
# 2.11 from Stepic
import string


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, new_login):
        if not Registration.is_included_sobaka(new_login):
            raise ValueError("Login must include at least one '@'")
        if not Registration.is_included_doth(new_login):
            raise ValueError("Login must include at least one '.'")
        self.__login = new_login

    @staticmethod
    def is_included_sobaka(login):
        return True if '@' in login else False

    @staticmethod
    def is_included_doth(login):
        return True if '.' in login else False

    @staticmethod
    def is_include_digit(password):
        for digit in password:
            if digit in string.digits:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        counter, flag2 = 0, False
        for l in password:
            if l.isupper():
                counter += 1
            if not l.isupper():
                flag2 = True
        return True if counter > 1 and flag2 else False

    @staticmethod
    def is_include_only_latin(password):
        for l in password:
            if l not in string.ascii_letters:
                if l not in string.digits:
                    return False
        return True

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            raise TypeError('Пароль должен быть строкой')
        if len(new_password) <= 4 or len(new_password) >= 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(new_password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(new_password):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not Registration.is_include_only_latin(new_password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        self.__password = new_password


me = Registration('mkurseev@yandex.ru', 'KUrseev1')
me.login = 'nkurseeva@yand.ry'
me.password = 'KKAHKJjjjn1'
print(me.login)
print(me.password)
