class AnimalConstruct:

    def __init__(self, name, eat_per_day, age):
        self.__name = name
        self.__eat_per_day = eat_per_day
        self.__age = age

    @property
    def eat_per_day(self):
        return self.__eat_per_day

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