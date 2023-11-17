import time
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(275)

    def current_score(self):
        self.write(f"Your score: {self.score}", False, "center", ('Arial', 14, 'normal'))
    def get_food(self):
        self.score += 1
        self.clear()
        self.current_score()

    def game_over(self):
        self.sety(0)
        self.write("Game is fucking over, Bitch!", False, "center", ('Arial', 20, 'normal'))

