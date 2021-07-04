from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "purple", "green", "blue"]

all_turtle = []
x = -230
y = -160
money = 10000
user_bet = screen.textinput("Make a bet", "choose which player will win")
for turtle_index in range(0, 6):
    new_tutle = Turtle("turtle")
    new_tutle.penup()
    new_tutle.color(colors[turtle_index])
    new_tutle.goto(x=x, y=y)
    y += 65
    all_turtle.append(new_tutle)

while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won the winning turtle was {winning_turtle}")
                is_race_on = False
            else:
                print(f"sorry you lost {winning_turtle} turtle won")
                is_race_on = False
        else:
            turtle.speed("slow")
            random_speed = randint(0, 10)
            turtle.forward(random_speed)

screen.mainloop()
