from turtle import *

half_side = 50
cross_size = 35
turn = 0
game = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
game_ended = False
speed = 20


def create_grids():
    """
    creates the grid for the tic tac toe
        |    |
        |    |
    ---- ---- ----
        |    |
        |    |
    ---- ---- ----
        |    |
        |    |

    :param a: Half side of the tic tac toe
    :return: nothing
    """

    line_turtle = Turtle()
    line_turtle.hideturtle()
    line_turtle.speed(speed)

    line_turtle.pensize(10)
    line_turtle.penup()
    line_turtle.goto(-3 * half_side, half_side)
    line_turtle.pendown()
    line_turtle.goto(+3 * half_side, half_side)

    line_turtle.penup()
    line_turtle.goto(-3 * half_side, -1 * half_side)
    line_turtle.pendown()
    line_turtle.goto(+3 * half_side, -1 * half_side)

    line_turtle.penup()
    line_turtle.goto(half_side, -3 * half_side)
    line_turtle.pendown()
    line_turtle.goto(half_side, 3 * half_side)

    line_turtle.penup()
    line_turtle.goto(-1 * half_side, 3 * half_side)
    line_turtle.pendown()
    line_turtle.goto(-1 * half_side, -3 * half_side)


def get_grid_position(x, y):
    """
    Given the position of the click, get the grid positions
    :param x: the x coordinate
    :param y: the y coordinate
    :param a: the half side
    :return: [cell x, cell y]
    """

    i = 1
    j = 1

    if x < -half_side:
        i = 0
    elif x > half_side:
        i = 2

    if y < -half_side:
        j = 2
    elif y > half_side:
        j = 0

    return (i, j)


def get_cell_center(i, j):
    """
    Returns the cell center coordinates from cell x, cell y
    :param i: cell x
    :param j: cell y
    :param a: half side
    :return: [center x, center y]
    """

    x = 0
    y = 0

    if i == 0:
        x = -2 * half_side
    elif i == 2:
        x = 2 * half_side

    if j == 0:
        y = 2 * half_side
    elif j == 2:
        y = -2 * half_side

    return (x, y)


def create_cross(i, j):
    """
    Creates a cross at a position
    :param i: cell x
    :param j: cell y
    :param a: half side
    :param b: cross size
    :return: nothing
    """

    x, y = get_cell_center(i, j)

    cross_turtle = Turtle()
    cross_turtle.speed(speed)
    cross_turtle.pensize(5)
    cross_turtle.hideturtle()

    cross_turtle.penup()
    cross_turtle.goto(x - cross_size, y + cross_size)
    cross_turtle.pendown()
    cross_turtle.goto(x + cross_size, y - cross_size)

    cross_turtle.penup()
    cross_turtle.goto(x + cross_size, y + cross_size)
    cross_turtle.pendown()
    cross_turtle.goto(x - cross_size, y - cross_size)


def create_zero(i, j):
    """
    Creates a zero at a position
    :param i: cell x
    :param j: cell y
    :param a: half side
    :param b: zero size
    :return: nothing
    """

    x, y = get_cell_center(i, j)

    zero_turtle = Turtle()
    zero_turtle.speed(speed)
    zero_turtle.pensize(5)
    zero_turtle.hideturtle()

    zero_turtle.penup()
    zero_turtle.goto(x, y - cross_size)
    zero_turtle.pendown()
    zero_turtle.circle(cross_size, steps=100)


def handle_click(x, y):
    """
    Handles when a click handles
    :param x: the x coordinate
    :param y: the y coordinate
    :return: nothing
    """

    global turn, game, game_ended

    (i, j) = get_grid_position(x, y)
    if game[j][i] != -1 or game_ended:
        return

    if turn == 0:
        create_cross(i, j)
    else:
        create_zero(i, j)

    game[j][i] = turn
    turn = 1 - turn

    status = check_game_ended()
    if status[0]:
        game_ended = True
        end_game_line = Turtle()
        end_game_line.pensize(15)
        end_game_line.speed(speed)
        end_game_line.hideturtle()
        end_game_line.color('#757575')

        (x1, y1) = get_cell_center(status[2][0], status[2][1])
        (x2, y2) = get_cell_center(status[3][0], status[3][1])
        end_game_line.penup()
        end_game_line.goto(x1, y1)
        end_game_line.pendown()
        end_game_line.goto(x2, y2)


def check_game_ended():
    """
    Checks if the game was finished
    :return: [True/False, [turn, cell_1, cell_2]]
    """

    global game

    for row in range(0, 3):
        if game[row][0] != -1 and game[row][0] == game[row][1] and game[row][0] == game[row][2]:
            return [True, game[row][0], (0, row), (2, row)]

    for column in range(0, 3):
        if game[0][column] != -1 and game[0][column] == game[1][column] and game[0][column] == game[2][column]:
            return [True, game[0][column], (column, 0), (column, 2)]

    if game[1][1] != -1 and game[0][0] == game[1][1] and game[0][0] == game[2][2]:
        return [True, game[1][1], (0, 0), (2, 2)]

    if game[1][1] != -1 and game[0][2] == game[1][1] and game[0][2] == game[2][0]:
        return [True, game[1][1], (0, 2), (2, 0)]

    return [False]


create_grids()
onscreenclick(handle_click)

mainloop()
