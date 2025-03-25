from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_len=5 , stretch_wid=1.2)
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.shape('square')
        self.paddle.goto(-350, 0)
       

    def move_up(self):
        self.paddle.fd(10)

    def move_down(self):
        self.paddle.fd(-10)





