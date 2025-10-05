#Вивести всі числа у зворотному порядку.
import random
lst = []
for i in range(20):
    lst.append(random.randint(-200,200))
print(lst)
lst.reverse()
print(lst)
