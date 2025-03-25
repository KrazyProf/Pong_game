from turtle import Turtle
FONTSIZE = 50
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


    def p1(self):
        self.goto(-150 , 150)
        self.write(arg=f'{self.p1_score}' , align='center' , font= ('Arial' , FONTSIZE , 'normal'))

    def p2(self):
        self.goto(150 , 150)
        self.write(arg=f'{self.p2_score}' , align='center' , font= ('Arial' ,FONTSIZE , 'normal'))
    
    def update_score(self, ball_cordinate):
        if ball_cordinate > 400:
            self.p2_score += 1
            self.clear()
            self.p2()
        else:
            self.p1_score += 1
            self.clear()
            self.p1()