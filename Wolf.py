from AnimalConstruct import *


class Wolf(AnimalConstruct):

    def __init__(self, name, eat_per_day, age):
        super().__init__(name, eat_per_day, age)
        self.__animal_type = 'волк'
        self.__biom = 'Тундра'
        self.__territory = 200  # м2
        self.__food = ['мясо']
        self.__predator = 'хищник'
        self.__sound = 'Вуф-Вуф'
        self.__isfeed = False

    def eat_food(self, foodtype, foodammount):
        if foodtype in self.__food:
            print('Ом-ном-ном')
            if foodammount >= self.eat_per_day:
                self.__isfeed = True
        else:
            print('Я не буду', foodtype)

    def do_noize(self):
        print(self.name, self.__sound)

    def play(self):
        print(self.__name, 'Удовлетворённо', self.__sound)

    @property
    def animal_type(self):
        return self.__animal_type

    @property
    def food(self):
        return self.__food

    @property
    def biom(self):
        return self.__biom

    @property
    def predator(self):
        return self.__predator

    @property
    def territory(self):
        return self.__territory

    @property
    def isfeed(self):
        return self.__isfeed

    @isfeed.setter
    def isfeed(self, value):
        if type(value) is bool:
            self.__isfeed = value
