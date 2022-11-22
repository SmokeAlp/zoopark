# Животные не вакцинированы, не кормить, клетки не открывать


class Giraffe:
    # общее
    animal_type = 'жираф'
    biom = 'саванна'
    territory = '100 км^2'
    food = ['кустарники', 'трава', 'фрукты']
    predator = 'травоядное'
    sound = 'руауавуагага(не слышно человеку)'

    def __init__(self, a_name, a_eat, a_age):
        # конкретное
        self.__name = a_name
        self.eat = a_eat
        self.__age = a_age
        self.__isFeed = False

    def eat_food(self, foodtype, foodammount):
        if foodtype in self.food:
            print('Ом-ном-ном')
            if foodammount >= self.eat:
                self.__isFeed = True
        else:
            print('Я не буду', foodtype)

    def do_noize(self):
        print(self.__name, self.sound)

    def play(self):
        print('Удовлетворённо', self.sound)
        
    @property
    def is_feed(self):
        return self.__isFeed
    
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, newname):
        if newname is str:
            self.__name = newname
        else:
            print('Надо нормальное имя!')
        
    @age.setter
    def age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print('Я живой')


class Horse:
    # общее
    animal_type = 'лошадь'
    biom = 'степь'
    territory = '200 м^2'
    food = ['сено', 'трава']
    predator = 'травоядное'
    sound = 'Шевелись, Плотва'
        
    def __init__(self, a_name, a_eat, a_age):
        # конкретное
        self.__name = a_name
        self.eat = a_eat
        self.__age = a_age
        self.__isFeed = False

    def eat_food(self, foodtype):
        if foodtype in self.food:
            print('Ом-ном-ном')
        else:
            print('Я не буду', foodtype)

    def do_noize(self):
        print(self.sound)

    def play(self):
        print('Удовлетворённо', self.sound)
        
    @property
    def isfeed(self):
        return self.__isFeed
    
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, newname):
        if newname is str:
            self.__name = newname
        else:
            print('Надо нормальное имя!')

    @age.setter
    def age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print('Я живой')


class Bear:
    # общее
    animal_type = 'медвед'
    biom = 'Тайга'
    territory = '6 км^2'
    food = ['мясо', 'ягоды']
    predator = 'всеядное'
    sound = 'Ну буфета здесь нет наверное...'
        
    def __init__(self, a_name, a_eat, a_age):
        # конкретное
        self.__name = a_name
        self.eat = a_eat
        self.__age = a_age
        self.__isFeed = False

    def eat_food(self, foodtype):
        if foodtype in self.food:
            print('Ом-ном-ном')
        else:
            print('Я не буду', foodtype)

    def do_noize(self):
        print(self.sound)

    def play(self):
        print('Удовлетворённо', self.sound)
        
    @property
    def isfeed(self):
        return self.__isFeed
    
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, newname):
        if newname is str:
            self.__name = newname
        else:
            print('Надо нормальное имя!')
        
    @age.setter
    def age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print('Я живой')
