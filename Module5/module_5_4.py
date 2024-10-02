class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)



    def __init__(self, name, umber_of_floors):
        self.name = name
        self.umber_of_floors = umber_of_floors

    def __len__(self):
        return self.umber_of_floors

    def __value__(self):
        return self.umber_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.umber_of_floors}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.umber_of_floors == other
        elif isinstance(other, House):
            return self.umber_of_floors == other.umber_of_floors
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def __lt__(self, other):
        if isinstance(other, int):
            return self.umber_of_floors < other
        elif isinstance(other, House):
            return self.umber_of_floors < other.umber_of_floors
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def __le__(self, other):
        if isinstance(other, int):
            return self.umber_of_floors <= other
        elif isinstance(other, House):
            return self.umber_of_floors <= other.umber_of_floors
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def __gt__(self, other):
        if isinstance(other, int):
            return self.umber_of_floors > other
        elif isinstance(other, House):
            return self.umber_of_floors > other.umber_of_floors
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def __ge__(self, other):
        if isinstance(other, int):
            return self.umber_of_floors >= other
        elif isinstance(other, House):
            return self.umber_of_floors >= other.umber_of_floors
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def __ne__(self, other):
        if isinstance(other, int):
            return self.umber_of_floors != other
        elif isinstance(other, House):
            return self.umber_of_floors != other.umber_of_floors
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def __add__(self, value):
        if isinstance(value, int):
            self.umber_of_floors += value
            return self
        elif isinstance(value, House):
            self.umber_of_floors += value.umber_of_floors
            return self
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.umber_of_floors += value
            return self
        elif isinstance(value, House):
            self.umber_of_floors += value.umber_of_floors
            return self
        else:
            print("Ошибка, операция не может быть выполненна")
            return self

    def go_to(self, new_floor):
        if new_floor > self.umber_of_floors or new_floor < 1:
            print(f'Этажа №{new_floor} не существует в доме: {self.name}')
        else:
            for i in range(new_floor):
                print(i + 1)
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)