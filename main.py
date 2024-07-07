from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.goUp, "Up")
screen.onkey(r_paddle.goDown, "Down")
screen.onkey(l_paddle.goUp, "w")
screen.onkey(l_paddle.goDown, "s")
screen.onkey(l_paddle.goUp, "W")
screen.onkey(l_paddle.goDown, "S")


game_is_on = True
while game_is_on:
  time.sleep(ball.getMoveSpeed())
  screen.update()
  ball.mov()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounceY()

  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
    ball.bounceX()

  if ball.xcor() > 380:
    ball.resetPosition()
    scoreboard.setLPoint()
  
  if ball.xcor() < -380:
    ball.resetPosition()
    scoreboard.setRPoint()

screen.exitonclick()