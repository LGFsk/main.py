class House:
    def __init__(self, name, umber_of_floors):
        self.name = name
        self.umber_of_floors = umber_of_floors

    def __len__(self):
        return self.umber_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.umber_of_floors}'

    def go_to(self, new_floor):
        if new_floor > self.umber_of_floors or new_floor < 1:
            print(f'Этажа №{new_floor} не существует в доме: {self.name}')
        else:
            for i in range(new_floor):
                print(i + 1)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
