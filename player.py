from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.game_speed = 0.1
        self.reset_player()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setposition(self.xcor(), new_y)

    def reset_player(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def increase_speed(self):
        if self.ycor() > FINISH_LINE_Y:
            self.game_speed *= 0.9
            self.reset_player()