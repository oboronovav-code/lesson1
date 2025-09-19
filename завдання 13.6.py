#6. Створити двовимірний масив (n times m), де (n) і (m) вводить користувач.
#Заповнити масив випадковими числами та знайти:
#- Суму елементів у кожному рядку.
#- Максимальний елемент у кожному стовпці.
import random
matrix = []
n = int(input("Введіть кількість рядків:"))
m = int(input("Введіть кількість стовпців:"))
for i in range(n):
    rows = []
    for y in range(m):
        chislo = random.randint(-500,500)
        rows.append(chislo)
    matrix.append(rows)
for rows in matrix:
    suma = sum(rows)
    print(rows, "Сума елементів цього рядка:",suma)
for j in range(m):
    max_el = []
    for x in range(n):
        max_el.append(matrix[x][j])
    print("MAX число в стовпці ",j+1,":", max(max_el))
