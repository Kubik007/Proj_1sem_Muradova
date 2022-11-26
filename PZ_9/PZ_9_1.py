# Дан словарь на 6 персон, найти и вывести наибольшее и наименьшее значение роста (в см.)
try:
    name = {"Арсений": 180, "Антон": 200, "Александр": 175, "Алексей": 150, "Андрей": 165, "Анатолий": 190}
    max_val = max(name.values())
    print(max_val)
    min_val = min(name.values())
    print(min_val)
except ValueError:
    print("Неправильный ввод")