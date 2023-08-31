from turtle import Turtle,Screen;

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clock():
       new_heading= tim.heading()+10
       tim.setheading(new_heading)


def move_clock():
   new_heading= tim.heading()-10
   tim.setheading(new_heading)
    

def move_clear():
    tim.clear()

def reset():
    tim.penup()
    tim.home()
    tim.pendown()
    
    
 

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_counter_clock)
screen.onkey(key='d', fun=move_clock)
screen.onkey(key='c', fun=move_clear)
screen.onkey(key='h', fun=reset)
screen.exitonclick()

