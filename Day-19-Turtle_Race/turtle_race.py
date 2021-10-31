import random
import turtle
from turtle import Turtle, Screen


def run_turtle(turt):
    if turt.xcor() < 250:
        step = random.randint(1, 10)
        turt.forward(step)


colors = ["red", "green", "orange", "yellow", "blue", "purple"]
turtles = []
y = 90
x = -230
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

for color in colors:
    new_turt = Turtle()
    new_turt.shape("turtle")
    new_turt.color(color)
    new_turt.penup()
    new_turt.goto(x, y)
    turtles.append(new_turt)
    y = y - 30

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle is going to win? Enter Color.").lower()
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turt in turtles:
        if turt.xcor() > 230:
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False

        run_turtle(turt)

screen.exitonclick()
