import turtle

import pandas as pd

NUM_STATES = 50
from turtle import Turtle, Screen

screen = Screen()
screen.title("US states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
states_df = pd.read_csv("50_states.csv")


def search_df(answer):
    for index,row  in states_df.iterrows():
            state = row.state
            x = row.x
            y = row.y
            if answer == state:
                return (x, y)


count = 0
answer_list = []
while count < 50:
    answer = screen.textinput(title=f"{count}/{NUM_STATES} states correct", prompt="What's another state's name?").title()
    pos = search_df(answer)
    if pos is not None and answer not in answer_list:
        state_turtle = Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(pos)
        state_turtle.write(answer)
        answer_list.append(answer)
        count += 1
screen.mainloop()
