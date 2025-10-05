#Знайти другий за величиною елемент.
import random
lst = []
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
a = max(lst)
lst.remove(a)
print("Друге за величиною число:",max(lst))