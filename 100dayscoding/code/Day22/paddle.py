from turtle import Turtle

class PaddleRight(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1, 5)
        self.penup()
        self.speed("fastest")
        self.goto(375, 0)

    def up(self):
        self.sety(self.ycor() + 30)

    def down(self):
        self.sety(self.ycor() - 30)

class PaddleLeft(PaddleRight):

    def __init__(self):
        super().__init__()
        self.goto(-375, 0)
