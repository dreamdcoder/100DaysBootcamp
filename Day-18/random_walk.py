import random
from turtle import  Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("firebrick")
timmy_the_turtle.pensize(15)

direction =[0,90,180,270]

screen = Screen()
screen.colormode(255)
for i in range (255):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        rgb = (r, g, b)
        timmy_the_turtle.color(rgb)
        timmy_the_turtle.setheading(random.choice(direction))
        timmy_the_turtle.forward(50)








screen.exitonclick()

