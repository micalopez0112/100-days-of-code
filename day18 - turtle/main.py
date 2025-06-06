from turtle import Turtle, Screen

# def turn_right():
#     timmy.forward(100)
#     timmy.right(90)
    
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

# for i in range(4):
#     turn_right()

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

SIDE_LENGTH = 50
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

timmy.speed(2)


for i in range(15):
    sides = i + 3
    angle = 360 / sides
    for _ in range(sides):
        timmy.color(colors[i % len(colors)])
        timmy.forward(SIDE_LENGTH)
        timmy.right(angle)


screen = Screen()
screen.exitonclick()

# import heroes as h

# print(h.get_heroes())