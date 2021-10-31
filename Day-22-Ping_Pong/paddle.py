from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.goto(pos)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() <= 340:
            new_x = self.xcor()
            new_y = self.ycor() + 20
            self.goto(new_x, new_y)

    def move_down(self):
        if self.ycor() >= -340:
            new_x = self.xcor()
            new_y = self.ycor() - 20
            self.goto(new_x, new_y)
