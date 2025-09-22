chislo = int(input("Введіть число: "))
kilkist = 0
for cifra in str(chislo):
    if int(cifra)%2 == 0:
        kilkist += 1

print("Кількість парних цифр числа: ", kilkist)

