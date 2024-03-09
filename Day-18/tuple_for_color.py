import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(10)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r,g,b)
    return colours

direction = [0, 90, 180, 270]

for i in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()