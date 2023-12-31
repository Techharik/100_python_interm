from turtle import Turtle

STARTING_POSITION =[(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__ (self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.addSegment(position)

    def addSegment(self,position):
            tim = Turtle()
            tim.color('white') 
            tim.shape('square')
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)
         
    def extend(self):
         self.addSegment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1 ,0,-1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x,new_y)
    
        self.segments[0].forward(20)
    

    def up(self):
        if self.head.heading()  != 270:
              self.head.setheading(90)

    def down(self):
        if self.head.heading()  != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()  != 0:
             self.head.setheading(180)

    def right(self):
        if self.head.heading()  != 180:
                self.head.setheading(0)

