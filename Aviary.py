class Aviary:

    def __init__(self, name, biom, territory):
        self.__aviary_name = name
        self.__biom = biom
        self.__territory = territory
        self.__animals = []
        self.__feeder = {'трава': 0, 'фрукты': 0, 'мясо': 0}

    def settle(self, animal):
        if self.__biom != animal.biom:
            print(animal.name, 'не подселился, не подходит биом.')
        elif self.__territory < animal.territory:
            print(animal.name, 'не подселился, нехватает места.')
        else:
            if len(self.__animals) != 0:
                if self.__animals[0].predator != 'травоядное':
                    if animal.animal_type != self.__animals[0].animal_type:
                        print(animal.name, 'не подселился, соседи не подходят.')
                    else:
                        self.__animals.append(animal)
                        self.__territory -= animal.territory
                        print(animal.name, 'успешно поселился в вольере!')
                elif animal.predator == 'травоядное':
                    self.__animals.append(animal)
                    self.__territory -= animal.territory
                    print(animal.name, 'успешно поселился в вольере!')
                else:
                    print(animal.name, 'не подселился, соседи не подходят.')
            else:
                self.__animals.append(animal)
                self.__territory -= animal.territory
                print(animal.name, 'успешно поселился в вольере!')

    def evict(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(animal.name, 'теперь бездомный!')
        else:
            print('Такого у нас не живёт...')

    def feed(self, foodtype, ammount):
        for key_g, values_g in self.__feeder.items():
            if key_g == foodtype:
                self.__feeder[key_g] += ammount
                print('теперь в кормушке', self.__feeder[key_g], 'кг', key_g)
        if len(self.__animals) != 0:
            for i in self.__animals:
                for key_g, values_g in self.__feeder.items():
                    for j in i.food:
                        if key_g == j:
                            if i.eat_per_day <= self.__feeder[key_g]:
                                if not i.isfeed:
                                    self.__feeder[key_g] -= i.eat_per_day
                                    i.isfeed = True
                                print(i.name, 'Наелся')
                            else:
                                print(i.name, 'Не наелся, надо ещё', i.eat_per_day - self.__feeder[key_g], 'кг', key_g)

    @property
    def animals(self):
        if len(self.__animals) != 0:
            print('В вольере живёт:')
            for i in self.__animals:
                print(i.animal_type, 'по имени', i.name)
        else:
            print('Вольер пуст')

    @property
    def feeder(self):
        print('Еда в кормушке:')
        for key_g, values_g in self.__feeder.items():
            print(key_g, values_g)
