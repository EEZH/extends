class Transport:
    def __init__(self, max_speed, size):
        self.max_speed = max_speed
        self.size = size

    def move(self):
        print("Двигаться")

    def turn(self):
        print("Повернуть")

    def stop(self):
        print("Остановиться")


class Weapon:
    def __init__(self, calibre):
        self.calibre = calibre

    def shoot(self):
        print("Выстрел")


class Car(Transport, Weapon):
    def __init__(self, max_speed, size, wheels_count, calibre):
        Transport.__init__(self, max_speed, size)
        Weapon.__init__(self, calibre)
        self.wheels_count = wheels_count

    def move(self):
        print("Ехать")

car = Car(180, 2, 4, 7.64)
print(car.max_speed)
car.move()
print(car.calibre)
