# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления площади, длины окружности и диаметра.

import math


class circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def diametr(self):
        return 2 * self.radius


r = int(input("Введите радиус круга: "))
obj = circle(r)
print("Площадь круга:", round(obj.area(), 2))
print("Длина окружности:", round(obj.perimeter(), 2))
print("Диаметр: ", round(obj.diametr(), 2))
