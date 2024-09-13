import time
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.color("white")

    def update_scoreboard(self):
        """Clears the current score and writes the new score"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=0)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=0)

    def r_point(self):
        """Increments the right side user score by 1"""
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        """Increments the left side user score by 1"""
        self.l_score += 1
        self.update_scoreboard()
