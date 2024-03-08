from turtle import Turtle, Screen

turtle_boy = Turtle()
turtle_boy.shape("turtle")
turtle_boy.color("red", "blue")

for i in range(4):
    turtle_boy.forward(100)
    turtle_boy.left(90)

screen = Screen()
screen.exitonclick()