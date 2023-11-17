import time
from turtle import Screen
from paddle import PaddleRight, PaddleLeft
from ball import Ball
from scoreboard import ScoreBoard, Border

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Bonk")
screen.listen()
screen.tracer(0)

paddle_right = PaddleRight()
paddle_left = PaddleLeft()

screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

ball = Ball()

score_l = ScoreBoard(-60)
score_r = ScoreBoard(30)
score_l.current_score()
score_r.current_score()

border = Border()

gameover = ScoreBoard(0)

speed = 0.05
ball.set_angle()
playing = True
while playing:
    screen.update()
    time.sleep(speed)
    ball.move()
    if paddle_right.distance(ball) < 50 and ball.xcor() > 350:
        ball.setheading(180 - ball.heading())
        speed -= 0.002
        if speed < 0.005:
            speed = 0.005
    elif paddle_left.distance(ball) < 50 and ball.xcor() < -350:
        ball.setheading(180 - ball.heading())
        speed -= 0.002
        if speed < 0.005:
            speed = 0.005
    elif ball.xcor() >= 420:
        score_l.get_point()
        ball.goto(0, 0)
        ball.set_angle()
        speed = 0.05
    elif ball.xcor() <= -420:
        score_r.get_point()
        ball.goto(0, 0)
        ball.set_angle()
        speed = 0.05
    if score_r.score == 5 or score_l.score == 5:
        playing = False
        gameover.game_over()


screen.exitonclick()