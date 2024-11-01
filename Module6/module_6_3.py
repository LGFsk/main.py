class Horse():
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super(Horse, self).__init__()

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle():
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super(Eagle, self).__init__()

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super(Pegasus, self).__init__()

    def move(self, dx, dy):
        x_distance = super().run(dx)
        y_distance = Eagle.fly(self, dy)
        return x_distance, y_distance

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()