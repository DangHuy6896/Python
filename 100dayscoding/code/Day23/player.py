from turtle import Turtle


MOVE_DISTANCE = 11
MOVE_DISTANCE_FAST = 30
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.7, 0.7)
        self.penup()
        self.sety(-280)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE + 2)

    def left(self):
        if self.xcor() <= -290:
            self.setx(self.xcor() - 0)
        else:
            self.setx(self.xcor() - 10)

    def right(self):
        if self.xcor() >= 290:
            self.setx(self.xcor() + 0)
        else:
            self.setx(self.xcor() + 10)

    def up_faster(self):
        self.forward(MOVE_DISTANCE_FAST)

    def down_faster(self):
        self.backward(MOVE_DISTANCE_FAST)

    def finish_lvl(self):
        self.setx(0)
        self.sety(-280)