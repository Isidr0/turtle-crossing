from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.turtlesize(1, 2)
        self.starting_y = (random.randint(-200, 280))
        self.starting_pos = (300, self.starting_y)
        self.penup()
        self.goto(self.starting_pos)
        self.new_x = 0


    def move_car(self):
        self.new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.setposition(self.new_x, self.ycor())

    def increase_speed(self):
        self.new_x = self.xcor() - MOVE_INCREMENT
        self.setposition(self.new_x, self.ycor())
