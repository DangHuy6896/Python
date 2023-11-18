from turtle import Turtle
from random import randint, choice

COLORS = ["crimson", "orange red", "sandy brown","light coral", "gold", "forest green", "royal blue", "dark violet"]
MOVE_INCREMENT = 1
THE_OUTSIDER_COLORS = ["black", "white"]
THE_COLOR = choice(THE_OUTSIDER_COLORS)
X = []
for p in range(320, 1000):
    X.append(p)
Y = []
for q in range(-220, 221, 20):
    Y.append(q)


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_cars()


    def create_cars(self):
        new_car = Turtle()
        new_car.color(THE_COLOR)
        new_car.penup()
        new_car.shapesize(1, 1.5)
        new_car.shape("square")
        new_car.setheading(180)
        new_car.goto(choice(X), choice(Y))
        self.cars.append(new_car)
        for n in range(24):
            self.create_car()


    def create_car(self):
        new_car = Turtle()
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.shapesize(1, 1.5)
        new_car.shape("square")
        new_car.setheading(180)
        new_car.goto(choice(X), choice(Y))
        self.cars.append(new_car)

    def move(self):
        global THE_COLOR
        if THE_COLOR == "black":
            self.cars[0].forward(30 + MOVE_INCREMENT)
        elif THE_COLOR == "white":
            self.cars[0].forward(1 + MOVE_INCREMENT)
        if self.cars[0].xcor() < -320:
            self.cars[0].goto(choice(X), choice(Y))
            THE_COLOR = choice(THE_OUTSIDER_COLORS)
            self.cars[0].color(THE_COLOR)

        for car in self.cars[1:9]:
            car.forward(3 + MOVE_INCREMENT)
            if car.xcor() < -320:
                car.goto(choice(X), choice(Y))
                car.color(choice(COLORS))
        for car in self.cars[9:17]:
            car.forward(4 + MOVE_INCREMENT)
            if car.xcor() < -320:
                car.goto(choice(X), choice(Y))
                car.color(choice(COLORS))
        for car in self.cars[17:24]:
            car.forward(5 + MOVE_INCREMENT)
            if car.xcor() < -320:
                car.goto(choice(X), choice(Y))
                car.color(choice(COLORS))
        for car in self.cars[24:]:
            car.forward(6 + MOVE_INCREMENT)
            if car.xcor() < -320:
                car.goto(choice(X), choice(Y))
                car.color(choice(COLORS))

    def lvl_up(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT += 0.5

    def next_lvl_1(self):
        self.create_car()

    def next_lvl_2(self):
        for _ in range(2):
            self.create_car()