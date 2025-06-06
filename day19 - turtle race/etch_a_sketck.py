from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def right():
    tim.setheading(tim.heading() - 10)
    
def left():
    tim.setheading(tim.heading() + 10)
    
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkey(key="w", fun=left)
screen.onkey(key="s", fun=right)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="d", fun=move_forward)
screen.onkey(key="c", fun=clear)


screen.exitonclick()