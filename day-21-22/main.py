from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# Prends une trace des animations et les met à zero (Les annules)
screen.tracer(0)
screen.title("Pong Game")

r_UP = "Up"
r_DOWN = "Down"

l_UP = "s"
l_DOWN = "w"

RIGHT_PADDLE = (350, 0)
LEFT_PADDLE = (-350, 0)

r_paddle = Paddle(RIGHT_PADDLE)
l_paddle = Paddle(LEFT_PADDLE)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(fun=r_paddle.move_up, key=r_UP)
screen.onkey(fun=r_paddle.move_down, key=r_DOWN)

screen.onkey(fun=l_paddle.move_up, key=l_UP)
screen.onkey(fun=l_paddle.move_down, key=l_DOWN)

# Quand je desactive les animations je dois avoir une sorte de drapeau pour affciher
# le contenu de l'écran et ceci se fait dans une boucle while
game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move_ball()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collison with r_paddle and r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect R paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
