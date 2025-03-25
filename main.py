from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


# Setting Up Screen 
screen = Screen()
screen.setup(width=800 ,height=600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)


# Creating paddles
left_paddle = Paddle(x_cor=-360 , y_cor=0)
right_paddle = Paddle(x_cor=360 , y_cor=0)

# creating ball
ball = Ball()
score = Score()

# Defining OnKey methods
screen.onkey(key="w" , fun=left_paddle.move_up)
screen.onkey(key="s" , fun=left_paddle.move_down)
screen.onkey(key="Up" , fun=right_paddle.move_up)
screen.onkey(key="Down" , fun=right_paddle.move_down)


while True:
# Updating the screen
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    # Detecting collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detecting whether the ball is out of bounds
    if ball.xcor() > 400 or ball.xcor() < -400:
        score.update_score(ball.xcor())
        ball.reset()

    # Detecting collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    
screen.exitonclick()