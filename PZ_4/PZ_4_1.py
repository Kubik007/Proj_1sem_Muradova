# Дано вещественное число Х и целое число N(>0). Найти значение выражения 1+Х+Х^2/(2!)+...+Х^N/(N!).
try:
    x = float(input())
    n = int(input())
    sum_ = 0
    i = 0
    while i <= n:
        s = 1
        k = i
        while k:
            s *= k
            k -= 1
        sum_ += x ** i / s
        i = i + 1
    print(sum_)
except ValueError:
    print('Ошибка')

