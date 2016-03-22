from turtle import *

a = 50
b = 35

# Turn Variable
# 0 : X
# 1 : O
turn = 0

# Creating a grid dictionary which will
# contain which symbol is in it
# -1 : empty
# 0 : X
# 1 : O
grid = dict()
grid[(0, 0)] = -1
grid[(0, 1)] = -1
grid[(0, 2)] = -1
grid[(1, 0)] = -1
grid[(1, 1)] = -1
grid[(1, 2)] = -1
grid[(2, 0)] = -1
grid[(2, 1)] = -1
grid[(2, 2)] = -1


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
    global turn, grid

    # Get the cell index
    i, j = get_cell_from_x_y(x, y)

    if grid[(i, j)] == -1:
        grid[(i, j)] = turn

        # For now make an x on the cell
        if turn == 0:
            create_x_in_cell(i, j)
            turn = 1
        else:
            create_o_in_cell(i, j)
            turn = 0

        who_won = check_game_ended()


def get_cell_from_x_y(x, y):
    # From the x and y coordinate of a click, get the cell indices
    # Check where x lies and assign i
    if x < -a:
        i = 0
    elif x > a:
        i = 2
    else:
        i = 1
    # Check where y lies and assign j
    if y < -a:
        j = 2
    elif y > a:
        j = 0
    else:
        j = 1

    return (i, j)

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
    x_turtle.speed(0)

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
    o_turtle.speed(0)

    o_turtle.penup()
    o_turtle.goto(xc, yc - b)
    o_turtle.pendown()

    o_turtle.circle(b, steps=20)


def check_game_ended():
    # In all cases below, if the values are actually same, return that value
    # This indicates who won the game

    # Check if all 3 are same (and not -1) in a row. Then loop through all rows
    for row in range(0, 3):
        if (grid[(0, row)] == grid[(1, row)]
            and grid[(0, row)] == grid[(2, row)]
            and grid[(0, row)] != -1):
            return grid[(0, row)]

    # Check if all 3 are same (and not -1) in a column. Then loop through all columns
    for column in range(3):
        if (grid[(column, 0)] == grid[(column, 1)]
            and grid[(column, 0)] == grid[(column, 2)]
            and grid[(column, 0)] != -1):
            return grid[(column, 0)]

    # Check for left diagonal
    if (grid[(0, 0)] == grid[(1, 1)] and grid[(0, 0)] == grid[(2, 2)]
        and grid[0, 0] != -1):
        return grid[(0, 0)]

    # Check for right diagonal
    if (grid[(2, 0)] == grid[(1, 1)] and grid[(2, 0)] == grid[(0, 2)]
        and grid[2, 0] != -1):
        return grid[(2, 0)]

    # If you are here means no one won, return -1
    return -1

create_grid()

onscreenclick(handle_click)
mainloop()