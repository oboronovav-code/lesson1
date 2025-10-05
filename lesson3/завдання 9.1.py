#Створити список із 20 чисел.

import random
lst = []
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)