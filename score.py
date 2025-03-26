from turtle import Turtle
FONTSIZE = 80
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.p1()
        self.p2()
        # self.display()


    def p1(self):
        self.goto(-100 ,200)
        self.write(arg=f'{self.p1_score}' , align='center' , font= ('Courier' , FONTSIZE , 'normal'))

    def p2(self):
        self.goto(100 , 200)
        self.write(arg=f'{self.p2_score}' , align='center' , font= ('Courier' ,FONTSIZE , 'normal'))
    
    def update_score(self, ball_cordinate):
        if ball_cordinate > 400:
            self.p1_score += 1
            self.clear()
            self.p1()
            self.p2()
        elif ball_cordinate < -400:
            self.p2_score += 1
            self.clear()
            self.p1()
            self.p2()
    
    # def display(self):

    #     self.setheading(270)
    #     self.goto(0,400)
    #     for _ in range(40):
    #         self.fd(10)
    #         self.penup()
    #         self.fd(10)
    #         self.pendown()
    #     self.penup()