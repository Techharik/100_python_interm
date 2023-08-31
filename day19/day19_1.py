from turtle import Turtle, Screen;
import random

screen = Screen()


screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet", prompt="What is your bet color? ")

colors= ['red','green','yellow']

all_turtle=[]
 
 
for turtle_index in range(0,3):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=-50+(turtle_index *30))
    all_turtle.append(tim)
    
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f'You won, The {wining_color} turtle is the winnser')
                is_race_on = False
            else:
                print(f'You Lose, The {wining_color} turtle is the winnser')
                is_race_on = False
        else:
            turtle.forward(random.randint(0,10))






screen.exitonclick()