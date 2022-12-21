from Aviary import *
from Bear import *
from Wolf import *

b1 = Bear('Kosolapiy', 3, 12)
b2 = Bear('Medved', 3, 11)
b3 = Bear('Medvezhonok', 2, 6)
w1 = Wolf('Hromoy', 2, 5)
a1 = Aviary('av', 'Тундра', 1000)

b2.name = 'Shatyn'
print('')

a1.settle(b1)
a1.settle(w1)
a1.settle(b2)
a1.settle(b3)
a1.animals
a1.evict(b3)
a1.feed('мясо', 5)
a1.feed('мясо', 2)
a1.feeder
print('')

print(b1.name, 'наелся?', b1.isfeed)
b1.eat_food('мясо', 12)
print(b1.name, 'наелся?', b1.isfeed)
