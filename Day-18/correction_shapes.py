from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', "DeepSkyBlue", 'LightSeaGreen', 'Wheat', "SlateGray", "SeaGreen"]

def draw_shape(num_angle):
    angle = 360 / num_angle
    for i in range(num_angle):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()