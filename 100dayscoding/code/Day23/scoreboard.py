from turtle import Turtle

FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-285, 265)
        self.score = 1

    def current_score(self):
        self.write(arg=f"Level {self.score}", font=FONT)

    def next_lvl(self):
        self.score += 1
        self.clear()
        self.current_score()

    def game_over(self):
        self.sety(0)
        self.setx(0)
        self.color("black")
        self.write("Game is fucking over, Bitch!", False, "center", ('Arial', 25, 'normal'))

