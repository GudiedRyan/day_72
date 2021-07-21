from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, -310)
    
    def move_left(self):
        self.goto(self.xcor() - 30, self.ycor())
    
    def move_right(self):
        self.goto(self.xcor() + 30, self.ycor())
