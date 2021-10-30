import random

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 300)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def increase_score(self, text):
        if text == 'left':
            self.left_score += 1
        if text == 'right':
            self.right_score += 1
        self.update_score()



