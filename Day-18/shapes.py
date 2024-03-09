from turtle import Turtle, Screen

tim = Turtle()

def triangle():
    tim.color("sky blue")
    for i in range(3):
        tim.forward(100)
        tim.right(120)

def square():
    tim.color("green")
    for i in range(4):
        tim.forward(100)
        tim.right(90)

def pentagon():
    tim.color("purple")
    for i in range(5):
        tim.forward(100)
        tim.right(72)

def hexagon():
    tim.color("yellow")
    for i in range(6):
        tim.forward(100)
        tim.right(60)

def heptagon():
    tim.color("blue")
    for i in range(7):
        tim.forward(100)
        tim.right(51.4)

def octagon():
    tim.color("red")
    for i in range(8):
        tim.forward(100)
        tim.right(45)

def nonagon():
    tim.color("sky blue")
    for i in range(9):
        tim.forward(100)
        tim.right(40)

def decagon():
    tim.color("sky blue")
    for i in range(10):
        tim.forward(100)
        tim.right(36)

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
screen.exitonclick()