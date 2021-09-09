FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-270, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 14, "normal"))

    def add_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(-70, 0)
        self.write(f"GAME OVER", align="left", font=FONT)