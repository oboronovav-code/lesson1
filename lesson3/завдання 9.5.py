#Вивести елементи, що рівні мінімальному.
import random
lst = []
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
a = min(lst)
for j in lst:
    if j == a:
        print(lst.pop(lst.index(j)))