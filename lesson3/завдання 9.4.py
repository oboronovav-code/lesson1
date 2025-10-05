#Замінити всі елементи, більші за 100, на 100.
import random
lst = []
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
for j in range(20):
    if lst[j] > 100:
        lst[j] = 100
print(lst)