from Aviary import *
from Bear import *
from Wolf import *
from Giraffe import *
from Horse import *

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
print('')

a1.feed('мясо', 5)
a1.feeder
a1.isfeed()
print('')

a2 = Aviary('avi', 'Степь', 350)
g1 = Giraffe('Мелман', 3, 11)
h1 = Horse('Плотва', 4, 6)
a2.settle(g1)
a2.settle(h1)
print('')

a2.feed('трава', 5)
a2.feed('фрукты', 1)
print('')
a2.do_noize()

b1.isfeed = False
print(b1.name, 'наелся?', b1.isfeed)
b1.eat_food('мясо', 12)
print(b1.name, 'наелся?', b1.isfeed)
