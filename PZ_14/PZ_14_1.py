import re

a = open('expansion.txt', 'r', encoding='utf-8')
a_1 = a.read()
a.close()
form = re.findall(r"\b(.xls|.xml|.html|.css|.py)", a_1)
print("Документы: ", form)
print("Количество элементов:", len(form))
