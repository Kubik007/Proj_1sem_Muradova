#Даны три числа. Найти среднее них(то есть число, расположенное между наименьшим и наибольшим)
a = input()
b = input()
c = input()
try:
    int(a)
    int(b)
    int(c)
    if a<c and c<b:
        print(c)
    elif b<a and a<c:
        print(a)
    else:
        print(b)
except ValueError:
    print('Ошибка')