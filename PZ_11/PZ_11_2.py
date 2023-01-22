# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке


f1 = open('text18-18.txt', encoding='UTF-8')
info = f1.read()
f1.close()

print(info)

four = " ".join(info.split("\n")[:4])
a = 0
for i in four:
    if i in "—.,!?:;…":
        a += 1
print("Количество знаков пунктуации в первых четырех строках: ", a)

f1 = open('text18-18.txt', encoding='UTF-8')
l = f1.readlines()
j = l[::-1]
f1.close()

f2 = open('text18-18_new.txt', 'w', encoding='UTF-8')
f2.writelines(j)
f2.close()

