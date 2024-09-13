import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(player.move_up,"Up")

    # IF YOU WANT THE TURTLE TO MOVE LEFT AND RIGHT.
    # Changes would have to be made to account for where player crosses finish line.
    # screen.onkeypress(player.move_left, "Left")
    # screen.onkeypress(player.move_right, "Right")

    Name = car.create_car()
    car.move()

    # Detects if car collides with player
    for cars in car.all_cars:
        if player.distance(cars) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detects if player crosses finish line
    if player.distance(0,300) < 10:
        player.setposition(0,-280)
        car.level_up()
        scoreboard.points()

screen.exitonclick()






