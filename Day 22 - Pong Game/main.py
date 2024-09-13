from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball_speed = 0.1

turtle = Turtle()
screen = Screen()
screen.title("My Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

r_paddle.move_right()
l_paddle.move_left()
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
        ball.move()

#     Detect collision with r_paddle and checks if ball went past paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_paddle()
        ball_speed *= 0.9

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_right()
        ball_speed = 0.1

    #     Detect collision with l_paddle and checks if ball went past paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()
        ball_speed *= 0.9

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_left()
        ball_speed = 0.1


screen.exitonclick()