from turtle import Turtle, Screen
from random import randint, shuffle

width = 500
height = 400
offset = 30
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=width, height=height, startx=None, starty=100)
screen.colormode(255)

is_race_on = False
turtles = []
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].pu()
    turtles[i].goto(x = -width / 2 + offset, y = offset * (i - (len(colors) - 1) / 2))
    turtles[i].color(colors[i])
    turtles[i].speed("fastest")

user_bet = ""
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle "
                                "will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    shuffle(turtles)
    for turtle in turtles:
        if turtle.xcor() > width / 2 - offset:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        else:
            turtle.forward(randint(0, 10))

screen.exitonclick()
