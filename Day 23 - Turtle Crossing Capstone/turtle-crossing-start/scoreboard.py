from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(x= -200, y=260)
        self.score = 1
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def points(self):
        """Increases the score/level by 1"""
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        """Shows game over screen with final level reached"""
        self.clear()
        self.setposition(x=0, y=0)
        self.write(f"   GAME OVER \nFinal Level: {self.score}", align="center", font=FONT)