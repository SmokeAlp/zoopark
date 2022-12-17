from AnimalConstruct import *


class Horse(AnimalConstruct):
        
    def __init__(self, name, eat_per_day, age):
        super().__init__(name, eat_per_day, age)
        self.__animal_type = 'лошадь'
        self.__biom = 'степь'
        self.__territory = 200  # м2
        self.__food = ['сено', 'трава']
        self.__predator = 'травоядное'
        self.__sound = 'Шевелись, Плотва'
        self.__isFeed = False

    def eat_food(self, foodtype, foodammount):
        if foodtype in self.__food:
            print('Ом-ном-ном')
            if foodammount >= self.eat_per_day:
                self.__isFeed = True
        else:
            print('Я не буду', foodtype)

    def do_noize(self):
        print(self.__sound)

    def play(self):
        print('Удовлетворённо', self.__sound)

    @property
    def animal_type(self):
        return self.__animal_type

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
    def isFeed(self):
        return self.__isFeed
