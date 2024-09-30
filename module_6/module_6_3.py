class Horse:
    x_distance = 0
    sound1 = 'Frrr'

    def run(self, dx):
        self.x_distance = self.x_distance+dx

class Eagle:
    y_distance = 0
    sound2 = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance = self.y_distance+dy

class Pegasus(Horse, Eagle):

    def __init__(self):
        self.sound = super().sound1
        self.sound = super().sound2

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()