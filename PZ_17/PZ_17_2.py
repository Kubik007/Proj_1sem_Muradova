# �������� �������� ������ "������������ ��������" � ��� ������������ ��� �������� ������� "����������" � "��������".
# � ������ "������������ ��������" ����� ����� ��������, ����� ��� ������������ �������� � ���������� �����,
# � ������ ���������� ����� ����� ���� ���������� �������� � ������.

class Transport:
    def __init__(self, max_rate):
        self.max_rate = max_rate

    def drive(self):
        print("����")


class Avto(Transport):
    def __init__(self, max_rate, wheels=4):
        super().__init__(max_rate)
        self.__wheels = wheels

    def open_doors(self):
        print("����� ���������")

    def close_doors(self):
        print("����� ���������")


class Motocycle(Transport):
    def __init__(self, max_rate, wheels=2, helmet=1):
        super().__init__(max_rate)
        self.__wheels = wheels
        self.__helmet = helmet
        self.__with_carriage = False

    def add_carriage(self):
        self.__with_carriage = True
        print("��������� �������")

    def remove_carriage(self):
        self.__with_carriage = False
        print("������ �������")


car = Avto(180)
car.open_doors()
car.close_doors()
car.drive()

moto = Motocycle(120, helmet=2)
moto.add_carriage()