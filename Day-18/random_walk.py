from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(10)
tim.speed(0)

colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', "DeepSkyBlue", 'LightSeaGreen', 'Wheat', "SlateGray", "SeaGreen"]

direction = [0, 90, 180, 270]

for i in range(300):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()