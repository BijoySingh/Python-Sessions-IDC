from turtle import *

my_turtle = Turtle()

my_turtle.color('#ff0000')

# my_turtle.penup()
"""
for count in range(0, 4):
    my_turtle.forward(100)

    my_turtle.left(90)
"""
#
# for count in range(0, 40):
#     my_turtle.forward(50)
#     my_turtle.left(20)
#
#
#
# def drawTriangle(side):
#     for count in range(0, 3):
#         my_turtle.forward(side)
#         my_turtle.left(120)
#
#
# my_turtle.forward(100)
# my_turtle.left(37)
# my_turtle.forward(50)
#
# my_turtle.goto(0, 0)

"""
Write a function drawRightAngleTriangle(base, height)


"""
#
# def drawRightAngleTriangle(base, height):
#     my_turtle.forward(base)
#     my_turtle.left(90)
#     my_turtle.forward(height)
#     my_turtle.goto(0, 0)
#
# drawRightAngleTriangle(100, 100)
"""
Make your turtle's pen size different
my_turtle.pensize(something)


goto and start at 0,0 -----100----- penup

goto and pendown at 0, 20 -----100----- penup

goto and pendown at 0, 40 -----100-----

Draw hamburger icon
"""

my_turtle.pensize(5)  # Change width of pen

def drawHamburger():

    my_turtle.goto(0, 0)
    my_turtle.forward(100)
    my_turtle.penup()

    my_turtle.goto(0, 20)
    my_turtle.pendown()
    my_turtle.forward(100)
    my_turtle.penup()

    my_turtle.goto(0, 40)
    my_turtle.pendown()
    my_turtle.forward(100)
    my_turtle.penup()


drawHamburger()
mainloop()
