# -*- coding: utf8 -*-
# Составить генератор (yield), который преобразует все буквенные символы в строчные.
def letters(low: str):
    for n in low:
        yield n.lower()


a = input("Введите стороку: ")
print("".join(letters(a)))