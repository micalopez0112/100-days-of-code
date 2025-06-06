import cologram
import turtle as t
import random

# rgb_colors = []
# colors = cologram.extract('./cologram.jpg', 30)

# print(colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
color_list = [(0,255,255), (255,0,255), (255,255,0), (255,0,0), (0,255,0), (0,0,255)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

number_of_dots = 100


for dot_count in range(1,number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
