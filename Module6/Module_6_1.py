class Animal():
    alive = True
    fed = False

    def eat(self, food):
        self.food = Plant
        if (food.edible) is True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        elif (food.edible) is False:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
        else:
            print("Ошибка")


class Plant():
    edible = False


class Mammal(Animal):
    def __init__(self, name):
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        self.edible = False
        self.name = name


class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
