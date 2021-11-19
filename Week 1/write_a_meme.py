"""
file: write-a-meme.py
description: "RUN TOM RUN!"
language: python3
author: Bardh Rushiti, br3004@rit.edu
"""

import math
import turtle


def init(font_size=10, speed=5):
    """
    Initializes the drawing window

    :param font_size the size of the word

    :pre: position (0,0), heading east, pen down
    :post: position (0,0), heading east, pen up
    :return: None
    """

    turtle.title("Run Tom Run!")
    turtle.penup()
    window = turtle.Screen()
    window.screensize()
    window.setup(width=1.0, height=1.0)
    turtle.back(font_size * 60)
    turtle.speed(speed)
    turtle.showturtle()


def draw_T(font_size=10):
    """
    Draws the letter 'T'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    # Preps for drawing
    turtle.pendown()

    turtle.fd(font_size * 10)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)

    turtle.fd(font_size * 4)
    turtle.left(90)

    turtle.fd(font_size * 8)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 8)
    turtle.left(90)
    turtle.fd(font_size * 4)

    turtle.right(90)
    turtle.fd(font_size * 2)

    # Post condition: Pen is up, and preps the space for next letter
    turtle.penup()
    turtle.right(90)
    turtle.fd(font_size * 12)


def draw_O(font_size=10):
    """
    Draws the letter 'O'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    # Preps for drawing
    turtle.pendown()

    for i in range(4):
        turtle.fd(font_size * 10)
        turtle.right(90)

    turtle.penup()
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.left(90)
    turtle.pendown()

    for i in range(4):
        turtle.fd(font_size * 6)
        turtle.right(90)

    # Post condition: Pen is up, and preps the space for next letter
    turtle.penup()
    turtle.left(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 10)


def draw_M(font_size=10):
    """
    Draws the letter 'M'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    # Preps for drawing
    turtle.pendown()

    turtle.fd(font_size * 2)
    turtle.right(60)
    turtle.fd(font_size * 8/math.sqrt(3) * 2)
    turtle.left(120)
    turtle.fd(font_size * 8/math.sqrt(3) * 2)
    turtle.right(60)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 10)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 6)
    turtle.left(150)
    turtle.fd(font_size * 6/math.sqrt(3) * 2)
    turtle.right(60)
    turtle.fd(font_size * 2.3)
    turtle.right(60)
    turtle.fd(font_size * 6 / math.sqrt(3) * 2)
    turtle.left(150)
    turtle.fd(font_size * 6)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 10)

    # Post condition: Pen is up, and preps the space for next letter
    turtle.penup()
    turtle.right(90)
    turtle.fd(font_size * 14)


def draw_R(font_size=10):
    """
    Draws the letter 'R'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    # Preps for drawing
    turtle.pendown()

    turtle.fd(font_size * 5)
    turtle.circle(font_size * -2.5, extent=180)
    turtle.fd(font_size * 3)
    turtle.left(90)

    turtle.left(45)
    turtle.fd(font_size * 7)
    turtle.right(135)
    turtle.fd(font_size * 2)
    turtle.right(45)
    turtle.fd(font_size * 4)
    turtle.left(135)
    turtle.fd(font_size * 3)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 10)

    turtle.penup()
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.left(90)
    turtle.back(font_size * 2)
    turtle.right(90)

    turtle.pendown()
    turtle.fd(font_size * 2.5)
    turtle.circle(font_size * -.75, extent=180)
    turtle.fd(font_size * 2.5)
    turtle.right(90)
    turtle.fd(font_size * 1.5)

    # Post condition: Pen is up, and preps the space for next letter
    turtle.penup()
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 8)


def draw_U(font_size=10):
    """
    Draws the letter 'U'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    # Preps for drawing
    turtle.pendown()

    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 5)
    turtle.circle(font_size * 3, extent=180)
    turtle.fd(font_size * 5)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 5)
    turtle.circle(font_size * -5, extent=180)
    turtle.fd(font_size * 5)
    turtle.right(90)

    # Post condition: Pen is up, and preps the space for next letter
    turtle.penup()
    turtle.fd(font_size * 12)


def draw_N(font_size=10):
    """
    Draws the letter 'N'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    # Preps for drawing
    turtle.pendown()
    turtle.fd(font_size * 2)
    turtle.right(60)
    turtle.fd(font_size * 2 * 7 / math.sqrt(3))
    turtle.left(150)
    turtle.fd(font_size * 7)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 10)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(60)
    turtle.fd(font_size * 2 * 7 / math.sqrt(3))
    turtle.left(150)
    turtle.fd(font_size * 7)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 10)
    turtle.right(90)

    # Post condition: Pen is up, and preps the space for next letter
    turtle.penup()
    turtle.fd(font_size * 10)


def draw_space(font_size=10):
    """
    Draws the space between words (100 pixels)

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    # Preps the space for next letter
    turtle.penup()
    turtle.fd(font_size * 10)


def draw_exclamation(font_size=10):
    """
    Draws '!'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    turtle.pendown()

    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 6)
    turtle.right(90)
    turtle.fd(font_size * 2)
    turtle.right(90)
    turtle.fd(font_size * 6)

    turtle.penup()
    turtle.back(font_size * 8)
    turtle.right(90)

    turtle.pendown()
    for i in range(4):
        turtle.fd(font_size * 2)
        turtle.right(90)

    turtle.penup()
    turtle.left(90)
    turtle.fd(font_size * 8)
    turtle.right(90)
    turtle.fd(font_size * 4)


def draw_RUN(font_size=10):
    """
    Draws the letter 'N'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    draw_R(font_size)
    draw_U(font_size)
    draw_N(font_size)


def draw_TOM(font_size=10):
    """
    Draws the letter 'T'

    :param font_size the size of the word

    :pre: enough space for drawing this letter, heading east, pen up
    :post:  enough space for drawing the next letter, heading east, pen up
    :return: None
    """

    draw_T(font_size)
    draw_O(font_size)
    draw_M(font_size)


def draw_run_tom_run(font_size):
    """
    Draws the phrase "RUN TOM RUM!"

    :param font_size the size of the word

    :return: None
    """

    draw_RUN(font_size)
    draw_space(font_size)
    draw_TOM(font_size)
    draw_space(font_size)
    draw_RUN(font_size)
    draw_exclamation(font_size)


def main():
    """
    Main function

    :return:
    """

    FONT_SIZE = 10
    init(FONT_SIZE, speed=10)
    draw_run_tom_run(FONT_SIZE)
    turtle.mainloop()


if __name__ == "__main__":
    main()
