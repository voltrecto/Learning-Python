from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.speed = 0

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, random.randint(-250, 280))
        new_car.setheading(180)
        self.cars_list.append(new_car)

    def move_car(self):
        for car in self.cars_list:
            car.forward(STARTING_MOVE_DISTANCE + self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT


