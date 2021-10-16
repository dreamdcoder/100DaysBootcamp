from turtle import Turtle, Screen

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):

        for positions in STARTING_POS:
            self.add_body(positions)

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_STEP)
        print(self.head.xcor(), self.head.ycor())

    def add_body(self, position):
        new_seg = Turtle()
        new_seg.shape("square")
        new_seg.speed("fastest")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snake_body.append(new_seg)

    def extend(self):
        new_seg_x = self.snake_body[-1].xcor()
        new_seg_y = self.snake_body[-1].ycor()
        self.add_body((new_seg_x, new_seg_y))

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for snake in self.snake_body:
            snake.goto(700,700)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
