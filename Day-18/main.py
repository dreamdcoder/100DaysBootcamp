import random
from turtle import  Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("firebrick")


# for _ in range(3):
#     timmy_the_turtle.right(120)
#     timmy_the_turtle.forward(100)

# for _ in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
#
# for _ in range(6):
#     timmy_the_turtle.right(60)
#     timmy_the_turtle.forward(100)
#
# for _ in range(8):
#     timmy_the_turtle.right(45)
#     timmy_the_turtle.forward(100)
#
# for _ in range(12):
#     timmy_the_turtle.right(30)
#     timmy_the_turtle.forward(100)

screen = Screen()
screen.colormode(255)
for i in range (3,13):
    if 360 % i == 0:
        angle = 360/i
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        rgb = (r, g, b)
        for _ in range(i):
            timmy_the_turtle.color(rgb)
            timmy_the_turtle.right(angle)
            timmy_the_turtle.forward(100)








screen.exitonclick()

