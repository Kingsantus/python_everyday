from turtle import Turtle, Screen
tim = Turtle()
tim.color("black", "blue")
for i in range(4):
    tim.forward(200)
    tim.left(90)

tim.left(45)
tim.forward(282.8427)
tim.left(135)
tim.forward(200)
tim.left(135)
tim.forward(282.8427)
screen = Screen()
screen.exitonclick()