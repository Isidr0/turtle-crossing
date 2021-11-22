import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.bgcolor("white")
screen.title("Turtler")
screen.setup(width=600, height=600)
screen.listen()
car_list = []


# allow player to move up and down
screen.onkeypress(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(player.game_speed)
    screen.update()

    if player.ycor() > 280:
        scoreboard.add_level()
        player.increase_speed()

    # generate random cars
    random_car = random.randint(1, 5)
    if game_is_on and random_car == 2:
        car_manager = CarManager()
        car_list.append(car_manager)

    # move the randomly generated cars
    for car in car_list:
        if scoreboard.level == 1:
            car.move_car()
        if scoreboard.level > 1:
            car.increase_speed()
        if car.xcor() < -300:
            car_list.remove(car)
            car.hideturtle()
        # detect collision with cars
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()



    # turtle reaches top of screen. reset position and level up. car speed increase.

screen.exitonclick()


