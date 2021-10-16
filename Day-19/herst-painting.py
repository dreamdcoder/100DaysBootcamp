import random, colorgram
from turtle import Turtle, Screen

colors = colorgram.extract('image.jpg', 30)
rgb_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

print(rgb_colors)

timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")

screen = Screen()
screen.colormode(255)
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)

for _ in range(10):
    y = timmy_the_turtle.ycor()
    initial_x = timmy_the_turtle.xcor()
    for _ in range(10):
        timmy_the_turtle.dot(20, random.choice(rgb_colors))
        x = timmy_the_turtle.xcor()
        timmy_the_turtle.setx(x + 50)
    timmy_the_turtle.setx(initial_x)
    timmy_the_turtle.sety(y + 50)


screen.exitonclick()
