"""
sunstar.py

Authors: Bardh Rushiti
         Prakhar Gupta

id: br3004, pg9349

This program is for CSCI - 603 Assignment Week3

This program uses Turtle module to make sunstar
"""

# Importing modules

import turtle
import math
import re


def draw_poly(sides: int, len: int, level: int, angle: int):
    """
    Draws polygon of side n and call recursive functions draw_side for design

    :param  len     length
            sides   sides of the polygon
            angle   deviation angle
            level   level of recursion

    :return: total turtle drawn length

    :pre:  totallength (Zero)
    :post: totallength (length of each shape * sides)
    """

    totalLength = 0
    for _ in range(sides):
        turtle.right(360 / sides)
        totalLength = draw_side(len, level, angle)

    return totalLength * sides


def draw_side(len: int, level: int, angle: int):
    """
    Draws the recursive pattern to form sunstar

    :param  len     length
            angle   deviation angle in degrees
            level   level of recursion

    :return: acc_len  total length moved by a turtle to make one side

    :pre:  accumulator length   Zero
    :post: accumulator length   length of shape
    """

    acc_len = 0  # Accumulator length zero
    if level == 1:  # Base recursion case
        turtle.forward(len)
        return acc_len + len
    else:  # For all other levels
        acc_len += draw_side(len / 4, 1, angle)
        turtle.left(angle)
        acc_len += draw_side(len / ((math.cos(math.radians(angle)) * 4)),
                             level - 1, angle)
        turtle.right(2 * angle)
        acc_len += draw_side(len / ((math.cos(math.radians(angle)) * 4)),
                             level - 1, angle)
        turtle.left(angle)
        acc_len += draw_side(len / 4, 1, angle)
    return acc_len


def check_type(temp, exp, param):
    """
    Checks input for wrong input type

    :param  temp    input string
            exp     regular expression
            param   the input parameter

    :return: integer converted input

    """

    while (exp.fullmatch(temp) == None):
        print(f"Value must be a int You entered {type(temp)}")
        temp = input("Please enter a positive integer for " + param + ": ")
    return int(temp)


def init():
    """
    Setting turtle configs

    :pre: position (0,0), heading east, pen up
    :post: position (-150,0), heading north, pen down

    :return: None

    """

    turtle.penup()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.forward(-150)
    turtle.pendown()


def main():
    """
    Main function
    """

    pattern = r"[0-9]+"  # RE pattern for all digits check
    exp = re.compile(pattern)

    temp = input("Please enter a positive integer for sides: ")
    sides = check_type(temp, exp, "sides")  # checking side

    temp = input("Please enter a positive integer for length: ")
    length = check_type(temp, exp, "length")  # checking length

    temp = input("Please enter a positive integer for levels: ")
    levels = check_type(temp, exp, "levels")  # checking levels

    if levels > 1:
        temp = input("Please enter a positive integer for deviation "
                     "angle in degrees: ")
        dev_angle = check_type(temp, exp,
                               "deviation angle in degrees")  # checking angle
    else:
        dev_angle = 0

    init()  # settling up turtle configs

    totalLength = draw_poly(sides, length, levels, dev_angle)

    print("Total length: " + str(totalLength))

    turtle.mainloop()


if __name__ == '__main__':
    main()
