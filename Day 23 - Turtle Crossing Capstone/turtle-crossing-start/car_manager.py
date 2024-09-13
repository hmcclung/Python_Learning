from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates random colored cars along the Y axis on the right side of the screen"""
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.setheading(180)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        """Moves cars forward"""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        """Increases the speed of the cars"""
        self.car_speed += MOVE_INCREMENT
