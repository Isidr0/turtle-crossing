import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
screen.bgcolor("white")
screen.title("Turtler")
screen.setup(width=600, height=600)
screen.listen()
car_list = []

# allow player to move up and down
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # generate random cars
    random_car = random.randint(1, 10)
    if game_is_on and random_car == 2:
        car_manager = CarManager()
        car_list.append(car_manager)

    # move the randomly generated cars
    for car in car_list:
        car.move_car()
        if car.xcor() < -300:
            car_list.remove(car)
        # detect collision with cars
        if player.distance(car) < 20:
            game_is_on = False

    # turtle reaches top of screen. reset position and level up. car speed increase.
    if player.ycor() > 280:
        player.reset_player()
        car_manager.speed_up_car()
        print(car_manager.new_x)


