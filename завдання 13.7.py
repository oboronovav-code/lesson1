#7. Задано одновимірний масив із 20 випадкових чисел у діапазоні від -100 до
#100.
#- Видалити всі елементи масиву, які кратні 10.
#- Знайти суму елементів масиву, які розташовані між першим і останнім
#від’ємними числами.
import random
lst = []
lst1 = []
for i in range(20):
    lst.append(random.randint(-100, 100))
for a in lst:
    if a%10 == 0:
        lst.remove(a)

for a in lst:
    if a<0:
        lst1.append(a)
b = lst1[0]
c = lst1[-1]
for a in lst:
    if a>0 and lst.index(a) > lst.index(b) and lst.index(a) < lst.index(c):
        lst1.append(a)
suma = sum(lst1) - b - c
print("Відфільтрований список:",lst, "\nСума елементів масиву, які розташовані між першим і останнім від’ємними числами:",suma)

