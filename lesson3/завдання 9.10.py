# Визначити кількість чисел, що дорівнюють середньому значенню.
import random
lst = []
a = 0
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
ser_suma = sum(lst)//20
print("Середнє значення :", ser_suma)
for j in lst:
    if j == ser_suma:
        a += 1
print("Кількість елементів, що рівні середньому значенню: ",a)