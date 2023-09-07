from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake Game')
screen.tracer(0)
starting_position =[(0,0),(-20,0),(-40,0)]

segments =[]
for position in starting_position:
    tim = Turtle()
    tim.color('white')
    tim.shape('square')
    tim.penup()
    tim.goto(position)
    segments.append(tim)


is_game_on =True

while is_game_on:
    
    time.sleep(0.1)
    for seg in range(len(segments)-1 ,0,-1):screen.update()
        new_x = segments[seg -1].xcor()
        new_y = segments[seg -1].ycor()
        segments[seg].goto(new_x,new_y)
    
    segments[0].forward(20)
    segments[0].left(90)






screen.exitonclick()





