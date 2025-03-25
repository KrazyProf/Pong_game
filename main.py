from turtle import Turtle, Screen
from paddle import Paddle

# Setting Up Screen 
screen = Screen()
screen.setup(width=800 ,height=800)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)


# Creating paddles
paddle = Paddle()

# Defining OnKey methods
screen.onkey(key="Up" , fun=paddle.move_up)
screen.onkey(key="Down" , fun=paddle.move_down)

while True:
# Updating the screen
    screen.update()





screen.exitonclick()