# �������� ����� �����, ������� ����� ������� ������� � ������ ��� ���������� �������, ����� ���������� � ��������.

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


r = int(input("������� ������ �����: "))
obj = circle(r)
print("������� �����:", round(obj.area(), 2))
print("����� ����������:", round(obj.perimeter(), 2))
print("�������: ", round(obj.diametr(), 2))