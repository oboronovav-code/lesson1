#Скласти новий список, у якому всі елементи помножені на 3.
import random
lst = []
lst1 = []
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
for j in range(20):
    lst1.append(3*lst[j])
print(lst1)