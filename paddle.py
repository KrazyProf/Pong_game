from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_body = []
        self.make_paddle()
        self.head = self.paddle_body[0]


    def make_paddle(self):
        for i in range(3):
            paddle = Turtle()
            paddle.color('white')
            paddle.shape('square')
            paddle.penup()
            paddle.goto(0 , -20 * i)
            self.paddle_body.append(paddle)
    
    def move_up(self):

        for i in range(len(self.paddle_body)- 1 , 0 , -1):
            self.paddle_body[i].goto(self.paddle_body[i - 1].position())
        
        self.head.setheading(90)
        self.head.fd(10)