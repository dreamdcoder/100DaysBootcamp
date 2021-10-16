import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("firebrick")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(10)


def anticlockwise():
    tim.left(10)


def clear():
    tim.reset()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=clockwise)
screen.onkey(key='d', fun=anticlockwise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
