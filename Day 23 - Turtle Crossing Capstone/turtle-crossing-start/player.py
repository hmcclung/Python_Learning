from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """Moves the player up the screen"""
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    # IF YOU WANT THE TURTLE TO MOVE LEFT AND RIGHT
    # def move_right(self):
    #     self.setheading(0)
    #     self.forward(20)

    # IF YOU WANT THE TURTLE TO MOVE LEFT AND RIGHT
    # def move_left(self):
    #     self.setheading(180)
    #     self.forward(20)
