from turtle import Turtle
alignment="center"
fonts=("Courier",24,"normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0
    self.color("White")
    self.penup()
    self.hideturtle()
    self.goto(0,270)
    self.update_scoreboard()

  def game_over(self):
    self.goto(0,0)
    self.write("Game Over",align=alignment,font=fonts)
    
  def update_scoreboard(self):
    self.write(f"Score : {self.score}",align=alignment,font=fonts)

    
  def increase_score(self):
    self.score+=1
    self.clear()
    self.update_scoreboard()
