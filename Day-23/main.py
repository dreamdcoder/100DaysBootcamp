import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
p1 = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=p1.move_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    # detect collison
    for car in car_manager.cars_list:
        if car.distance(p1) < 20:
            game_is_on = False
            score_board.game_over()
    if p1.check_finish_line():
        p1.player_reset()
        score_board.update_scoreboard()
        car_manager.level_up()


screen.exitonclick()
