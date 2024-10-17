class Vehicle():
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__power = power

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}")

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__power}")

    def get_color(self):
        print(f"Цвет: {self.__color}")

    def set_color(self, new_color):
        count = 0
        self.new_color = new_color
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() in i.lower():
                self.__color = new_color
                count = count + 1

        if count == 0:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
