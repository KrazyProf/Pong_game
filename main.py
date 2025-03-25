from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


# Setting Up Screen 
screen = Screen()
screen.setup(width=800 ,height=800)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)


# Creating paddles
left_paddle = Paddle(x_cor=-350 , y_cor=0)
right_paddle = Paddle(x_cor=350 , y_cor=0)

# creating ball
ball = Ball()

# Defining OnKey methods
screen.onkeypress(key="Up" , fun=left_paddle.move_up)
screen.onkeypress(key="Down" , fun=left_paddle.move_down)
screen.onkeypress(key="w" , fun=right_paddle.move_up)
screen.onkeypress(key="s" , fun=right_paddle.move_down)

while True:
# Updating the screen
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

screen.exitonclick()