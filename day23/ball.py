from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(0,0)

    def move(self,position):
        new_xpos = self.xcor()+position[0]
        new_ypos = self.ycor()+position[1]
        self.goto(new_xpos,new_ypos )
