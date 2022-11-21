# Животные не вакцинированы, не кормить, клетки не открывать

import random


class Giraffe:

    def __init__(self, a_name, a_eat, a_age):
        # общее
        self.Type = 'жираф'
        self.Biom = 'саванна'
        self.Territory = '100 км^2'
        self.Food = ['кустарники', 'трава', 'фрукты']
        self.Predator = 'травоядное'
        self.Sound = 'руауавуагага(не слышно человеку)'

        # конкретное
        self.Name = a_name
        self.Eat = a_eat
        self.Age = a_age

    def eat_food(self):
        print(self.Food[random.randint(0, 2)], 'Ом-ном-ном')

    def do_noize(self):
        print(self.Sound)

    def play(self):
        print('Удовлетворённо', self.Sound)


class Horse:

    def __init__(self, a_name, a_eat, a_age):
        # общее
        self.Type = 'лошадь'
        self.Biom = 'степь'
        self.Territory = '200 м^2'
        self.Food = ['сено', 'трава']
        self.Predator = 'травоядное'
        self.Sound = 'Шевелись, Плотва'

        # конкретное
        self.Name = a_name
        self.Eat = a_eat
        self.Age = a_age

    def eat_food(self):
        print(self.Food[random.randint(0, 1)], 'Ом-ном-ном')

    def do_noize(self):
        print(self.Sound)

    def play(self):
        print('Удовлетворённо', self.Sound)


class Bear:

    def __init__(self, a_name, a_eat, a_age):
        # общее
        self.Type = 'медвед'
        self.Biom = 'Россия'
        self.Territory = '6 км^2'
        self.Food = ['мясо', 'ягоды']
        self.Predator = 'всеядное'
        self.Sound = 'Ну буфета здесь нет наверное...'

        # конкретное
        self.Name = a_name
        self.Eat = a_eat
        self.Age = a_age

    def eat_food(self):
        print(self.Food[random.randint(0, 1)], 'Ом-ном-ном')

    def do_noize(self):
        print(self.Sound)

    def play(self):
        print('Удовлетворённо', self.Sound)
