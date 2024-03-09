import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r,g,b)
    return colours

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
num_of_dot = 100

for i in range(1, num_of_dot + 1):
    tim.dot(20, random_color())
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()