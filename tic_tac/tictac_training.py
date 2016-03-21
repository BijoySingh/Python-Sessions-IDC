from turtle import *

a = 50
b = 35

def create_grid():
    # The turtle which makes the grid
    lines = Turtle()

    # Visual appeal, increasing the pen size
    lines.pensize(10)
    lines.speed(0)

    # Top horizontal line
    lines.penup()
    lines.goto(-3*a, a)
    lines.pendown()
    lines.goto(3*a, a)

    # Bottom horizontal line
    lines.penup()
    lines.goto(-3*a, -a)
    lines.pendown()
    lines.goto(3*a, -a)

    # Left vertical line
    lines.penup()
    lines.goto(-a, -3*a)
    lines.pendown()
    lines.goto(-a, 3*a)

    # Right vertical line
    lines.penup()
    lines.goto(a, -3*a)
    lines.pendown()
    lines.goto(a, 3*a)

def handle_click(x, y):
    pass

def get_cell_from_x_y(x, y):
    pass

def get_cell_center(i, j):
    # Get the X coordinate of the center using i
    x = 0
    if i == 0:
        x = -2 * a
    elif i == 1:
        x = 0
    elif i == 2:
        x = 2 * a

    # Get the Y coordinate of the center using j
    y = 0
    if j == 0:
        y = 2 * a
    elif j == 1:
        y = 0
    elif j == 2:
        y = -2 * a

    # Return the output as (x, y)
    # This is a 'tuple', which lets you get the values
    # out in multiple variables directly
    return (x, y)


def create_x_in_cell(i, j):
    # Call the get_center function
    # Because the output is a tuple of size 2,
    # I can directly get it in variables xc, yc
    # Which are the center's x and y coordinate
    xc, yc = get_cell_center(i, j)

    # Create a new turtle for making the x
    # Remember it will be at 0,0 with pen down
    x_turtle = Turtle()

    # For appeal only
    x_turtle.pensize(5)

    # Make left diagonal line
    x_turtle.penup()
    x_turtle.goto(xc - b, yc + b)
    x_turtle.pendown()
    x_turtle.goto(xc + b, yc - b)

    # Make right diagonal line
    x_turtle.penup()
    x_turtle.goto(xc + b, yc + b)
    x_turtle.pendown()
    x_turtle.goto(xc - b, yc - b)

def create_o_in_cell(i, j):
    # Get center x, y
    # Same as in create x case
    xc, yc = get_cell_center(i, j)

    # Create a circle : Experiment with o_turtle.circle(b)
    # Notice (please do yourself) that the circle is not
    # created from the center, if you do goto center and then circle
    o_turtle = Turtle()
    o_turtle.pensize(5)

    o_turtle.penup()
    o_turtle.goto(xc, yc - b)
    o_turtle.pendown()

    o_turtle.circle(b, steps=50)


create_grid()
create_x_in_cell(1, 0)
create_o_in_cell(1, 1 )




mainloop()