import turtle as t
import random as r


class Molecule:
    '''
    a class that describes molecules, their speed and radius
    '''
    def __init__(self, r, speed, x, y, name = None):
        self.r = r
        self.speed = speed
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def show(self):
        t.up()
        t.goto(self.x, self.y)
        t.down
        t.fillcolor('red')
        t.begin_fill()
        t.circle(self.r)
        t.end_fill()
        t.up
        t.right(180)
        t.forward(self.r)
        t.down
        t.fillcolor('red')
        t.begin_fill()
        t.circle(self.r)
        t.end_fill()
        t.up
        t.left(120)
        t.forward(self.r)
        t.down
        t.fillcolor('black')
        t.begin_fill()
        t.circle(self.r)
        t.end_fill()
        t.up

    def move(self):
        self.x = self.x + r.randint(-1, 1) * self.speed
        self.y = self.y + r.randint(-1, 1) * self.speed