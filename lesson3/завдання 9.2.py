#Порахувати кількість чисел, що діляться на 2 або 5.
import random
lst = []
a = 0
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
for j in lst:
    if j%2 == 0 or j%5 == 0:
        a+=1
print("Кількість чисел, що діляться на 2 або 5: ",a) 