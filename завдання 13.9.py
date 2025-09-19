#9. Створити масив чисел і відсортувати його за модулем у порядку зростання.
import random
lst = []
lst1 = []
for i in range(10):
    lst.append(random.randint(-15, 15))
for y in lst:
    if y > 0 or y == 0:
        lst1.append(y)
    else:
        lst1.append(y*(-1))
lst1.sort()
print("Початковий список:",lst,"\nСписок відсортований зо модулями чисел:",lst1)
