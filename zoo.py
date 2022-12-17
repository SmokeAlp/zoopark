from Aviary import *
from Bear import *

b1 = Bear('kosolapiy', 3, 12)
a1 = Aviary('av', 'Тайга', 1000)
a1.settle(b1)
a1.settle(b1)
a1.settle(b1)
a1.settle(b1)
print(b1.isFeed)
b1.eat_food('мясо', 12)
print(b1.isFeed)
