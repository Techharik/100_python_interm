# print('Create a pong Game')
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)




r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.r_go_up,'Up')
screen.onkey(r_paddle.r_go_down,'Down')
screen.onkey(l_paddle.l_go_up,'w')
screen.onkey(l_paddle.l_go_down,'s')


game_ball = Ball()

game_is_on = True
ball_pos = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    game_ball.move((ball_pos,ball_pos))
    ball_pos+=10

  


screen.exitonclick()
