from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, x_cor , y_cor):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_len=5 , stretch_wid=1.2)
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.shape('square')
        self.xcor = x_cor
        self.ycor = y_cor
        self.paddle.goto(self.xcor , self.ycor)
       

    def move_up(self):
        self.paddle.fd(10)

    def move_down(self):
        self.paddle.fd(-10)





