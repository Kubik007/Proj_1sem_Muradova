# Создание базового класса "Транспортное средство" и его наследование для создания классов "Автомобиль" и "Мотоцикл".
# В классе "Транспортное средство" будут общие свойства, такие как максимальная скорость и количество колес,
# а классы наследники будут иметь свои уникальные свойства и методы.

class Transport:
    def __init__(self, max_rate):
        self.max_rate = max_rate

    def drive(self):
        print("Едем")


class Avto(Transport):
    def __init__(self, max_rate, wheels=4):
        super().__init__(max_rate)
        self.__wheels = wheels

    def open_doors(self):
        print("Двери открылись")

    def close_doors(self):
        print("Двери закрылись")


class Motocycle(Transport):
    def __init__(self, max_rate, wheels=2, helmet=1):
        super().__init__(max_rate)
        self.__wheels = wheels
        self.__helmet = helmet
        self.__with_carriage = False

    def add_carriage(self):
        self.__with_carriage = True
        print("Добавлена коляска")

    def remove_carriage(self):
        self.__with_carriage = False
        print("Убрана коляска")


car = Avto(180)
car.open_doors()
car.close_doors()
car.drive()

moto = Motocycle(120, helmet=2)
moto.add_carriage()
