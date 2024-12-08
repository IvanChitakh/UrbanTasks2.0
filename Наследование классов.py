class Animal:
    alive, fed = True, False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        eatAction = "съел" if food.edible else "не стал есть"
        print(f'{self.name} {eatAction} {food.name}')
        self.alive &= food.edible
        self.fed |= food.edible


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


wolf = Predator('Волк')
cow = Mammal('Корова')
rose = Flower('Роза')
orange = Fruit('Апельсин')

print(wolf.name)
print(rose.name)

print(wolf.alive)
print(cow.fed)
wolf.eat(rose)
cow.eat(orange)
print(wolf.alive)
print(cow.fed)
