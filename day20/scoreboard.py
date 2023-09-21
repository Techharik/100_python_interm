from turtle import Turtle

class Scoreboard(Turtle):
     def __init__(self):
          super().__init__()
          self.scores = 0
          self.color("white")
          self.penup()
          self.goto(0,270)
          self.hideturtle()
          self.update_score()    

     def update_score(self):
            self.write(f"Score : {self.scores}",align="center",font=("Arial",22,"normal"))
    

     def is_game_over(self):
          self.goto(0,0) 
          self.write("Game Over" ,align="center",font=("Arial",22,"normal") )
     
     def increase_score(self):
        self.scores += 1
        self.clear()
        self.update_score()

         
