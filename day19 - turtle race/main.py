from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
print(bet)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []

for index in range(0,len(colors)):
    new_tim = Turtle('turtle')
    new_tim.penup()
    new_tim.color(colors[index])
    new_tim.goto(x=-230, y=-100 + index * 30)
    turtles.append(new_tim)

if bet:
    is_race_on = True
    has_turned = [False] * len(turtles)  # new list to keep track of which turtles have turned

   
while is_race_on:
    for i, turtle in enumerate(turtles):
        if turtle.xcor() > 230 and not has_turned[i]: 
            turtle.setheading(180)
            has_turned[i] = True
        elif turtle.xcor() < -230 and has_turned[i]:  
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick() 