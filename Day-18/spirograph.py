import random
from turtle import  Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("firebrick")
timmy_the_turtle.speed("fastest")

direction =[0,90,180,270]

def get_random_color():
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        rgb = (r, g, b)
        return rgb

screen = Screen()
screen.colormode(255)
def draw_spiro_graph(gap_size):
        for i in range (int(360/gap_size)):
                timmy_the_turtle.color(get_random_color())
                timmy_the_turtle.circle(100)
                curr_heading=timmy_the_turtle.heading()
                timmy_the_turtle.setheading(curr_heading+gap_size)


draw_spiro_graph(13)









screen.exitonclick()

