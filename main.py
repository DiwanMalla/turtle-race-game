import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500,400)
screen.bgcolor("lightgray")
user_bet = screen.textinput("Guess winner","Make your bet. Choose colour")
colors = ["red","orange","yellow","green","blue","purple"]
while user_bet not in colors:
    print("Invalid color choice. Please choose from: red, orange, yellow, green, blue, purple")
    user_bet = screen.textinput("Guess winner", "Make your bet. Choose color (red, orange, yellow, green, blue, purple)")
i=0
y = -150
turtles = []
for color_turtle in colors:
    color_turtle = Turtle(shape="turtle")
    color_turtle.color(colors[i])
    color_turtle.penup()
    color_turtle.goto(-230,y)
    i+=1
    y+=40
    turtles.append(color_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor()>220:
            if turtle.pencolor() == user_bet.lower():
                print(f'Congratulations, you win bet. {turtle.pencolor()} win the race')
            else:
                print(f'You lost {turtle.pencolor()} win the race')
            is_race_on=False



screen.exitonclick()