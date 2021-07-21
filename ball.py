from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.vertical_val = 10
        self.horizontal_val = 10
        self.move_speed = 0.05
        self.goto(0, -290)

    def move(self):
        self.goto(self.xcor() + self.horizontal_val, self.ycor() + self.vertical_val)

    def side_wall_collision(self):
        self.horizontal_val *= -1

    def paddle_and_roof_collision(self):
        self.vertical_val *= -1

    def block_collision(self):
        self.vertical_val *= -1

    def out_of_bounds(self):
        self.goto(0, -290)
        self.paddle_and_roof_collision()
