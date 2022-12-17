class Bear:

    def __init__(self, name, eat_per_day, age):
        self.__animal_type = 'медвед'
        self.__biom = 'Тайга'
        self.__territory = 300  # м2
        self.__food = ['мясо', 'ягоды']
        self.__predator = 'всеядное'
        self.__sound = 'Ну буфета здесь нет наверное...'
        self.__name = name
        self.__eat_per_day = eat_per_day
        self.__age = age
        self.__isFeed = False

    def eat_food(self, foodtype, foodammount):
        if foodtype in self.__food:
            print('Ом-ном-ном')
            if foodammount >= self.__eat_per_day:
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
    def eat_per_day(self):
        return self.__eat_per_day

    @property
    def predator(self):
        return self.__predator

    @property
    def territory(self):
        return self.__territory

    @property
    def isfeed(self):
        return self.__isFeed

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) is int:
            if value >= 0:
                self.__age = value
            else:
                print('Я живой')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        if type(newname) is str:
            self.__name = newname
        else:
            print('Надо нормальное имя!')