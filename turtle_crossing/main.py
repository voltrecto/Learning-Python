import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player1 = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player1.go_up, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter % 6 == 0:
        car_manager.create_car()
    counter += 1

    car_manager.move_car()
    for car in car_manager.cars_list:
        if car.distance(player1) < 20 and car.ycor() - player1.ycor() < 20:
            game_is_on = False
            scoreboard.game_over()

    if player1.ycor() > 280:
        scoreboard.increase_level()
        player1.reset_position()
        car_manager.increase_speed()


screen.exitonclick()
