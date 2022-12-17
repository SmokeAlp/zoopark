class Aviary:

    def __init__(self, name, biom, territory):
        self.__aviary_name = name
        self.__biom = biom
        self.__territory = territory
        self.__animals = []
# разобраться с __ в свойствах животных

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

    @property
    def animals(self):
        for i in self.__animals:
            print(i.animal_type, 'по имени', i.name)