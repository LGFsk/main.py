class House:
    def __init__(self, name, umber_of_floors):
        self.name = name
        self.umber_of_floors = umber_of_floors

    def go_to(self, new_floor):
        if new_floor > self.umber_of_floors or new_floor < 1:
            print(f'Этажа №{new_floor} не существует в доме: {self.name}')
        else:
            for i in range(new_floor):
                print(i + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(4)
