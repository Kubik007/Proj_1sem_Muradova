# Описать функцию PowerA234(A, B, C, D), вычисляющую вторую, третью и четвертую
# степень числа A и возвращающую эти степени соответственно в переменные B, C и D (A —
# входной, B, C, D — выходные параметры; все параметры являются вещественными).
# С помощью этой функции найти вторую, третью и четвертую степень пяти данных чисел.
def function(x):
    numb_1 = pow(x, 1)
    numb_2 = pow(x, 2)
    numb_3 = pow(x, 3)
    numb_4 = pow(x, 4)
    return numb_1, numb_2, numb_3, numb_4

for i in range(5):
    a = float(input('Введите число '))
    step1, step2, step3, step4 = float(a), float(a), float(a), float(a)
    step_1, step_2, step_3, step_4 = function(step1)
    print('Вторая степень числа = ',step_2 )
    print('Третья степень числа = ',step_3 )
    print('Четвёртая степень числа = ',step_4 )