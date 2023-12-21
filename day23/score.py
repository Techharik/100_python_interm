from turtle import Turtle

class Scoreboard(Turtle):
     def __init__(self):
          super().__init__()
          self.scores_l = 0
          self.scores_r = 0

          self.color("white")
          self.penup()
          self.goto(0,270)
          self.hideturtle()
          self.update_score()    

     def update_score(self):
            self.write(f"{self.scores_l} : {self.scores_r}",align="center",font=("Arial",22,"normal"))
    

     def is_game_over(self):
          self.goto(0,0) 
         
          if self.scores_l > self.scores_r:
                self.write("Player 1 wins - Game Over " ,align="center",font=("Arial",22,"normal") )
          elif self.scores_l < self.scores_r:
                self.write("Player 2 wins - Game Over" ,align="center",font=("Arial",22,"normal") )
          else:
               self.write("Draw - Game Over" ,align="center",font=("Arial",22,"normal") )
     
     def increase_score_r(self):
        self.scores_r += 1
        self.clear()
        self.update_score()

     def increase_score_l(self):
        self.scores_l += 1
        self.clear()
        self.update_score()
