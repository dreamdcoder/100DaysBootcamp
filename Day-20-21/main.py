import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Cobra")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
        score.reset_score()
        snake.reset_snake()

    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
