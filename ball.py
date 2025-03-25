from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape('circle')
        self.ball.color('white')
    
    def move_ball(self):
        self.ball.goto(self.ball.xcor() + 10 , self.ball.ycor() + 10)
