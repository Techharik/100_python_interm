# print('Create a pong Game')
from turtle import Turtle,Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong Game")



rightPaddle= Turtle()
rightPaddle.shape('square')
rightPaddle.color('white')
rightPaddle.shapesize(stretch_wid=5,stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350,0)


def go_up():
    new_y = rightPaddle.ycor()+10
    rightPaddle.goto(rightPaddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up,'up')









screen.exitonclick()
