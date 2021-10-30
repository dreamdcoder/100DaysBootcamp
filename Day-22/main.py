import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard

STARTING_POS = [(-290, 0), (290, 0)]

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Cobra")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()
score_board = Scoreboard()

screen.listen()

screen.onkey(key="w", fun=paddle1.move_up)
screen.onkey(key="s", fun=paddle1.move_down)

screen.onkey(key="Up", fun=paddle2.move_up)
screen.onkey(key="Down", fun=paddle2.move_down)

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()

    if (ball.distance(paddle2) < 50 and ball.xcor() > 320) or (ball.distance(paddle1) < 50 and ball.xcor() < -320):
        ball.bounce_of_paddle()
    if ball.ycor() > 375 or ball.ycor() < -375:
        ball.bounce_of_wall()

    if ball.xcor() > 380 :
        ball.reset_position()
        score_board.increase_score('left')
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.increase_score('right')
screen.exitonclick()
