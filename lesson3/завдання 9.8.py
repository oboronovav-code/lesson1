#Порахувати суму додатних чисел.
import random
lst = []
a = 0
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
for j in lst:
    if j > 0:
        a += j
print(a)