from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "yellow", "blue", "purple", "indigo", "black"]

pos_y = -100

is_race_on = False

turtle_list = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=pos_y)
    pos_y += 40
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the winning color is: {winning_color}")
            else:
                print(f"You've won! the winning color is: {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.listen()

screen.exitonclick()
