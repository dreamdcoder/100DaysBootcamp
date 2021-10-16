import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars_list = []
        self.x = 300
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y = random.randint(-250, 250)
            x = 300
            new_car.goto((x, y))
            car_color = random.choice(COLORS)
            new_car.color(car_color)
            self.cars_list.append(new_car)

    def move_car(self):
        for car in self.cars_list:
            car.backward(self.car_speed)
            # print(car.xcor())
            if car.xcor() < -300:
                car.clear()
                car.goto(1000,1000)
                self.cars_list.remove(car)
        print(len(self.cars_list))

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
