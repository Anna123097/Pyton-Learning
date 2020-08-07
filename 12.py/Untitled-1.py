class Car:
    def __init__(self, color ='black', motors='Speed', passenger=None):
        self.color = color
        self.motors = motors
        self.passenger = passenger

    def Drive(self):
        print(f"Машина цвета {self.color}  c мотором {self.motors} с водителем {self.passenger.name} едет")

    def Stop(self):
        print("Машина стоит на месте")


class ANa:
    def __init__(self, name="Anna"):
        self.name=name
        

class Human:
    def __init__(self, name="Anna", sorname="Korbut"):
        self.name = name
        self.sorname = sorname

    def printInfo(self):
        print(f"{self.name} {self.sorname} ")


danik = Human("Danik", "Trotsenko")


anna = Human()


x = Car("yellow", 'strong', danik)
y = True

while y:
    tmp = input("Продолжить движение? ")
    if tmp == 'y':
        x.Drive()
    else:
        x.Stop()
        y = False