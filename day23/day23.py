# print('Create a pong Game')
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)




r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
game_ball = Ball()
game_score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.r_go_up,'Up')
screen.onkey(r_paddle.r_go_down,'Down')
screen.onkey(l_paddle.l_go_up,'w')
screen.onkey(l_paddle.l_go_down,'s')



game_is_on = True



while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_ball.move()

    if game_ball.ycor()>280 or game_ball.ycor() < -280:
        game_ball.bounce_y()
  

    if game_ball.distance(r_paddle) < 60 and game_ball.xcor()>340 or game_ball.distance(l_paddle) < 60 and game_ball.xcor()>-340:
        if game_ball.distance(r_paddle) < 60:
           game_ball.bounce_x()
           game_score.increase_score_r()
        
        if game_ball.distance(l_paddle) < 60:
            game_score.increase_score_l()
            game_ball.bounce_x()

    
    if game_ball.xcor()>380 or game_ball.xcor() < -380:
        game_score.is_game_over()
        game_is_on = False


screen.exitonclick()
