from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Inherits from Turtle class"""
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the score by clearing the screen and writing the new score"""
        self.clear()
        self.write(arg=f"Score = {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        """Adds 1 to the score and then calls the update_scoreboard function"""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Keeps track of the all-time high score and resets the current scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    # """Before implementing the reset function, this created the Game over screen"""
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER.", align=ALIGNMENT, font=FONT)
