import random
lst = []
lst1 = []
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
for j in lst:
    if index(j)%2 == 1:
        lst1.append(j)
print("Cереднє значення чисел на непарних позиціях: ", sum(lst1)/len(lst1))
