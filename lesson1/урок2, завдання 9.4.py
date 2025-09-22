n = int(input("Введіть значення n: "))
suma = 0
for i in range(1, n+1):
    suma += i**2
print("Сума квадратів чисел від 1 до n: ",suma)
