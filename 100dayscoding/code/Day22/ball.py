from turtle import Turtle
from random import choice

a = []
for n in range(1, 76):
    a.append(n)
for n in range(105, 166):
    a.append(n)
for n in range(195, 256):
    a.append(n)
for n in range(285, 346):
    a.append(n)
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def set_angle(self):
        self.setheading(choice(a))

    def move(self):
        self.forward(10)
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.setheading(360 - self.heading())

