# Дана строка. Преобразовать в ней все строчные буквы (как латинские, так и русские)
# в прописные, а прописные в строчные
try:
    a = input("Введите строку: ")
    print(a.swapcase())
except ValueError:
    print("Неправильный ввод")