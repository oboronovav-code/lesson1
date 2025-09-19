#10. Задано двовимірний масив (n times m). Реалізувати програму для пошуку
#&quot;сідлової точки&quot; в масиві (елемент, який є мінімальним у своєму рядку та
#максимальним у своєму стовпці). Якщо таких точок кілька, вивести всі.
import random
matrix = []
max_el = []
min_el = []
tochka = []
n = int(input("Введіть кількість рядків:"))
m = int(input("Введіть кількість стовпців:"))
for i in range(n):
    rows = []
    for y in range(m):
        chislo = random.randint(-500,500)
        rows.append(chislo)
    matrix.append(rows)
for rows in matrix:
    min_el.append(min(rows))
    print(rows)
for j in range(m):
    max_el_m = []
    for x in range(n):
        max_el_m.append(matrix[x][j])
    max_el.append(max(max_el_m))
for t in range(n):
    for k in range(m):
        if max_el[k] == min_el[t]:
            tochka.append(min_el[t])
print('"Сідлові точки" матриці:',tochka)
    
