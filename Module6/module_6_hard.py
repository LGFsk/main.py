class Figure():
    def __init__(self, color, sides):
        self.sides_count = 0
        self.__color: list = color
        self.__sides: list = sides
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
                and isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = [r, g, b]
        else:
            print('Цвет не может быть изменен, введено не целое число или вне RGB 0-255')

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            return False
        for i in sides:
            if not (isinstance(i, int) and i > 0):
                return False
        return True

    def get_sides(self):
        return list(self.sides)

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.sides = list(new_sides)

    pass


class Circle(Figure):
    def __init__(self, color, *sides):
        Figure.__init__(self, color, sides)
        self.sides_count: int = 1
        if len(self._Figure__sides) == self.sides_count:
            self.sides = list(self._Figure__sides) * self.sides_count
        else:
            self.sides = [1 for i in range(self.sides_count)]

    def __radius(self):
        return len(self) / 2 / 3.14

    def get_square(self):
        return self.__radius() * self.__radius() * 3.14 / 2


class Triangle(Figure):
    def __init__(self, color, *sides):
        Figure.__init__(self, color, sides)
        self.sides_count: int = 3
        if len(self._Figure__sides) == self.sides_count:
            self.sides = list(self._Figure__sides)
        else:
            self.sides = [1 for i in range(self.sides_count)]

    def get_square(self):
        a = 0.5 * len(self)
        return math.sqrt(a * (a - self.sides[0]) * (a - self.sides[1]) * (a - self.sides[2]))


class Cube(Figure):
    def __init__(self, color, *sides):
        Figure.__init__(self, color, sides)
        self.sides_count: int = 12
        if len(self._Figure__sides) == 1:
            self.sides = list(self._Figure__sides) * self.sides_count
        elif len(self._Figure__sides) == self.sides_count and self._Figure__sides[0] == sum(
                self._Figure__sides) / self.sides_count:
            self.sides = [self._Figure__sides[0]] * self.sides_count
        else:
            self.sides = [1 for i in range(self.sides_count)]

    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())