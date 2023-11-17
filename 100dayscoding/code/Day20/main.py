from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Fucking Game, Baby!")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
score.current_score()
speed = 0.09
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    if snake.head.distance(food) < 15:
        score.get_food()
        snake.extend()
        food.refresh()
        if score.score > 20:
            speed = 0.08
            if score.score > 40:
                speed = 0.07
                if score.score > 60:
                    speed = 0.06
                    if score.score > 80:
                        speed = 0.05
    if snake.head.xcor() > 298 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -299:
        game_is_on = False
        score.game_over()
    for m in snake.segments[1:]:
        if snake.head.distance(m) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()