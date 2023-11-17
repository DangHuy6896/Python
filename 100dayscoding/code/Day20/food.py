from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("tomato")
        self.speed("fastest")
        self.goto((randint(-28, 28) * 10), (randint(-28, 26) * 10))

    def refresh(self):
        self.goto((randint(-28, 28) * 10), (randint(-28, 26) * 10))