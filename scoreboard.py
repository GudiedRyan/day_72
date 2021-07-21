from turtle import Turtle

ALIGNMENT="center"
FONT = ("Courier", 35)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.show_lives()

    def show_lives(self):
        self.clear()
        self.goto(0, 290)
        self.write(f"Lives: {self.lives}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,290)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def win_game(self):
        self.goto(0,100)
        self.write("You win!", align=ALIGNMENT, font=FONT)