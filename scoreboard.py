from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Couriel", 80, "normal")

class Scoreboard(Turtle):

  def __init__(self) -> None:
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.updateScoreboard()
  
  def updateScoreboard(self):
    self.clear()
    self.goto(-100, 190)
    self.write(self.l_score, align = ALIGNMENT, font = FONT )
    self.goto(100, 190)
    self.write(self.r_score, align = ALIGNMENT, font = FONT )

  def setLPoint(self):
    self.l_score += 1
    self.updateScoreboard()
  
  def setRPoint(self):
    self.r_score += 1
    self.updateScoreboard()
  
