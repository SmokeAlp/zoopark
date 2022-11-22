# Животные не вакцинированы, не кормить, клетки не открывать

import random


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
        self.__age = a_age, 

    def eat_food(self, FoodType):
        if FoodType in self.food:
            print('Ом-ном-ном')
        else:
            print('Я не буду', FoodType)

    def do_noize(self):
        print(self.name, self.sound)

    def play(self):
        print('Удовлетворённо', self.sound)
        
    @Age.setter
    
    def Age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print('Я живой')
    
    @property
    
    def Age(self):
        return self.__age

    def Name(self):
        return self.__name

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

    def eat_food(self, FoodType):
        if FoodType in self.food:
            print('Ом-ном-ном')
        else:
            print('Я не буду', FoodType)

    def do_noize(self):
        print(self.sound)

    def play(self):
        print('Удовлетворённо', self.sound)
        
    @Age.setter
    
    def Age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print('Я живой')
    
    @property
    
    def Age(self):
        return self.__age

    def Name(self):
        return self.__name


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

    def eat_food(self, FoodType):
        if FoodType in self.food:
            print('Ом-ном-ном')
        else:
            print('Я не буду', FoodType)

    def do_noize(self):
        print(self.sound)

    def play(self):
        print('Удовлетворённо', self.sound)
        
    @Age.setter
    
    def Age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print('Я живой')
    
    @property
    
    def Age(self):
        return self.__age

    def Name(self):
        return self.__name
