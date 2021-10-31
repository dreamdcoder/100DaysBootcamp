from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-290,270)
        self.level = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.level +=1
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)


