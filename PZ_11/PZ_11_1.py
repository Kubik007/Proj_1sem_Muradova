# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов:


a = ['-5 0 10 25 -50 100']
f1 = open('PZ_11_1_f1.txt', 'w')
f1.writelines(a)
f1.close()

f2 = open('PZ_11_1_f2.txt', 'w')
f2.write('Исходные данные: ')
f2.writelines(a)
f2.close()

f1 = open('PZ_11_1_f1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f2 = open('PZ_11_1_f2.txt', 'a')
f2.write('\n')
f2.write('Количество элементов: ')
f2.write(str(len(k)))
f2.close()

f2 = open('PZ_11_1_f2.txt', 'a')
f2.write('\n')
f2.write('Среднее арифметическое элементов: ')
f2.write(str(sum(k)/len(k)))
f2.close()

f2 = open('PZ_11_1_f2.txt', 'a')
f2.write('\n')
f2.write('Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов: ')
for i in a:
    a[i] = int(a[i-1] + a[i+1])**2
f2.write(a[i])
f2.close()
