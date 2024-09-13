from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.go_up()
        self.go_down()

    def go_up(self):
        """Moves paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move_right(self):
        """Moves paddle right"""
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")

    def move_left(self):
        """Moves paddle left"""
        self.screen.listen()
        self.screen.onkey(self.go_up, "w")
        self.screen.onkey(self.go_down, "s")
