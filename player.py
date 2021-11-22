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
        self.reset_player()

    def move_up(self):
        new_y = self.ycor() + 10
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.setposition(self.xcor(), new_y)

    def reset_player(self):
        self.penup()
        self.goto(STARTING_POSITION)