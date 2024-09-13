import time
from turtle import Turtle

HEADING = 38
SPEED = 15


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.home()
        self.move()
        self.setheading(HEADING)

    def move(self):
        """Moves the ball forward at the specified SPEED"""
        self.forward(SPEED)
        # Other method of how to do it
        # new_x = self.xcor() +10
        # new_y = self.ycor() +10
        # self.goto(new_x, new_y)

    def bounce_wall(self):
        """Changes the heading of the ball upon collision with the wall"""
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def bounce_paddle(self):
        """Changes the heading of the ball upon collision with the paddles."""
        new_heading = 180 - self.heading()
        self.setheading(new_heading)
        self.forward(SPEED)

    def reset_right(self):
        """Resets the ball if it passes the right paddle"""
        self.home()
        self.setheading(180 - HEADING)
        self.forward(SPEED)

    def reset_left(self):
        """Resets the ball if it passes the left paddle"""
        self.home()
        self.setheading(HEADING)
        self.forward(SPEED)
        time.sleep(1)
