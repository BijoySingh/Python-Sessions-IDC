# Multiple Turtles in one window
from turtle import *

first_turtle = Turtle()
second_turtle = Turtle()
third_turtle = Turtle()

second_turtle.penup()
second_turtle.goto(0, 20)
second_turtle.pendown()

third_turtle.penup()
third_turtle.goto(0, 40)
third_turtle.pendown()

first_turtle.pensize(10)
second_turtle.pensize(10)
third_turtle.pensize(10)

first_turtle.forward(100)
second_turtle.forward(100)
third_turtle.forward(100)

mainloop()
