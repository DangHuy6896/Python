from turtle import Turtle, Screen


screen = Screen()
screen.setup(800, 600)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y = [125, 75, 25, -25, -75, -125]

for n in range(6):
    heo = Turtle("turtle")
    heo.color(colors[n])
    heo.penup()
    heo.goto(-380, y[n])











































screen.exitonclick()

