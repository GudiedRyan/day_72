from turtle import Screen
from ball import Ball
from paddle import Paddle
from blocks import Block, BlockRow
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=700)
screen.tracer(0)

screen.listen()

paddle = Paddle()

row_1 = BlockRow("red", 0)
row_2 = BlockRow("orange", 40)
row_3 = BlockRow("yellow", 80)
row_4 = BlockRow("green", 120)
row_5 = BlockRow("blue", 160)
row_6 = BlockRow("purple", 200)

rows = [row_1, row_2, row_3, row_4, row_5, row_6]
score = Scoreboard()
ball = Ball()

block_count = 0

screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if abs(ball.xcor()) > 280:
        ball.side_wall_collision()

    if ball.ycor() > 330:
        ball.paddle_and_roof_collision()

    if ball.distance(paddle) < 50 and ball.ycor() < -300:
        ball.paddle_and_roof_collision()
    
    if ball.ycor() < - 360:
        score.lives -= 1
        score.show_lives()
        if score.lives == 0:
            score.game_over()
            game_is_on = False
        ball.out_of_bounds()

    for row in rows:
        for block in row.blocks:
            if ball.distance(block) < 50 and block.active == True:
                block.change_color()
                ball.block_collision()
                block_count += 1

    if block_count == 42:
        screen.update()
        score.win_game()
        game_is_on = False
        

screen.exitonclick()