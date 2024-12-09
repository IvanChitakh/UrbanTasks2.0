import random


class Animal:
    live = True
    sound = None
    _degree_of_danger = 0
    _cords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):

        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._degree_of_danger < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _degree_of_danger = 3

    def dive_in(self, dz):
        self._cords[2] -= int(dz * (self.speed / 2))


class PoisonousAnimal(Animal):
    _degree_of_danger = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
