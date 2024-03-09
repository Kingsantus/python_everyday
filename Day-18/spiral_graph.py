import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r,g,b)
    return colours


def draw_spiralgraph(size_of_space):
    for i in range(int(360/size_of_space)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_space)

draw_spiralgraph(1)

screen = t.Screen()
screen.exitonclick()