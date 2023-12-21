from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0,0)
        self.x_move =10
        self.y_move =10

    def move(self):
        new_xpos = self.xcor()+self.x_move
        new_ypos = self.ycor()+self.y_move
        self.goto(new_xpos,new_ypos )
    
    def bounce_y(self):
        self.y_move *= -1 

    def bounce_x(self):
        self.x_move *=-1