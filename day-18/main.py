from turtle import Turtle, Screen

tinny = Turtle()

for _ in range(50):
    tinny.forward(10)
    tinny.penup()
    tinny.forward(10)
    tinny.pendown()


screen = Screen()

screen.exitonclick()
