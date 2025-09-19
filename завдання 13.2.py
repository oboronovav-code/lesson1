#2. Реалізувати програму для перевірки, чи є введене число простим. Якщо ні,
#знайти всі його дільники.
lst = []
dilnyk = []
chislo = int(input("Введіть число: "))
if chislo < 1 or chislo == 1:
    print("Ваше число не може бути простим")
else:
    for i in range(2, chislo+1):
        if chislo%i != 0:
            lst.append(i)
    if len(lst) == chislo-2:
        print("Ваше число просте")
    else:
        for y in range(1, chislo+1):
            if chislo%y == 0:
                dilnyk.append(y)
        print("Ваше число не просте.\nДільники вашого числа:",dilnyk)
