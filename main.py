from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800 ,height=800)
screen.bgcolor('black')
screen.tracer(0)

left_paddle = Paddle()
right_paddle = Paddle()

screen.listen()
screen.onkey(key='w' , fun=left_paddle.move_up)


while True:
    screen.update()
# left_paddle.goto(0 , 350)


screen.exitonclick()