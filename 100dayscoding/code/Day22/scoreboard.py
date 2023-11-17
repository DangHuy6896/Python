from turtle import Turtle

POSITION = [(0, 300), (0, 270), (0, 240), (0, 210), (0, 180), (0, 150), (0, 120), (0, 90), (0, 60), (0, 30), (0, 0), (0, -30), (0, -60), (0, -90), (0, -120), (0, -150), (0, -180), (0, -210), (0, -240), (0, -270), (0, -300)]

class ScoreBoard(Turtle):

    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(222)
        self.setx(side)
        self.score = 0

    def current_score(self):
        self.write(arg=f"{self.score}", font=('Arial', 50, 'normal'))

    def get_point(self):
        self.score += 1
        self.clear()
        self.current_score()

    def game_over(self):
        self.sety(0)
        self.color("tomato")
        self.write("Game is fucking over, Bitch!", False, "center", ('Arial', 20, 'normal'))

class Border():

    def __init__(self):
        self.yy = []
        self.create_border()



    def add_border(self, n):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(1, 0.3)
        new_segment.penup()
        new_segment.goto(n)
        self.yy.append(new_segment)

    def create_border(self):
        for n in POSITION:
            self.add_border(n)



