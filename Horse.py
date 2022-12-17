class Horse:
        
    def __init__(self, name, eat_per_day, age):
        self.__animal_type = 'лошадь'
        self.__biom = 'степь'
        self.__territory = 200  # м2
        self.__food = ['сено', 'трава']
        self.__predator = 'травоядное'
        self.__sound = 'Шевелись, Плотва'
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
