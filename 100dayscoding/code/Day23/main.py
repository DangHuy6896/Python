from scoreboard import ScoreBoard
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from turtle import Screen
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("gainsboro")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
screen.onkey(player.up_faster, "w")
screen.onkey(player.down_faster, "s")

car = CarManager()

score = ScoreBoard()
score.current_score()

speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car.move()
    if player.ycor() >= FINISH_LINE_Y:
        player.finish_lvl()
        score.next_lvl()
        car.next_lvl_1()
        car.lvl_up()
        speed *= 0.95
    for a in car.cars[0:]:
        for n in range(-220, 221, 20):
            if abs(player.ycor() - n) < 15 and a.distance(player) < 22:
                score.game_over()
                game_is_on = False
                break
    if score.score > 30:
        screen.bgcolor("slate gray")
        car.next_lvl_2()
    elif score.score > 20:
        screen.bgcolor("dark gray")
        car.next_lvl_1()
    elif score.score > 10:
        screen.bgcolor("silver")
        
screen.exitonclick()



