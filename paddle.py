from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, x_cor , y_cor):
        super().__init__()
        self.setheading(90)
        self.shapesize(stretch_len=5 , stretch_wid=1)
        self.penup()
        self.color('white')
        self.shape('square')
        self.xcor = x_cor
        self.ycor = y_cor
        self.goto(self.xcor , self.ycor)
       

    def move_up(self):
        self.fd(10)

    def move_down(self):
        self.fd(-10)





