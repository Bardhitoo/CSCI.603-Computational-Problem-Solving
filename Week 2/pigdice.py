"""
pigdice.py
Author: Bardh Rushiti, Prakhar Gupta

id: br3004, pg9349

This program is for CSCI -603 Assignment Week2

This program uses Turtle module to create a graphical representation of PIG game
"""

import random
import time
import turtle as t
from score import Keeper

keeper = Keeper()
MAX_SCORE = 20  # The maximum score where each player is aiming for
SIDE = 150
RADIUS = 3


def init(speed, name="Game"):
    """
    Initializes the drawing window

    :param speed: the speed of turtle
    :param name:  the title of the of turtle

    :return: None

    :pre: position (0,0), heading east, pen down
    :post: position (0,0), heading east, pen up
    """

    t.title(name)
    t.penup()

    screen = t.Screen()
    screen.setup(width=1.0, height=1.0, startx=None, starty=None)
    t.speed(speed)
    t.showturtle()


def draw_outline(length):
    """
    Draws a square in current direction

    :param length: how long the square sides should be.

    :return: None

    :pre:  heading right
    :post: heading right
    """
    t.pendown()
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)


def draw_one_dot(x, y, radius=1):
    """
    Draws the single dot in center
    :param x:       The x-coordinate of the dot
    :param y:       The y-coordinate of the dot
    :param radius:  The radius of the circle

    :return: None
    """
    t.penup()
    t.fd(x + radius)
    t.left(90)
    t.fd(y + radius)

    t.pendown()
    t.fillcolor('black')
    t.begin_fill()

    t.circle(radius=radius)
    t.end_fill()

    t.penup()
    t.fd(-y - radius)
    t.right(90)
    t.fd(-x - radius)


def draw_two_dots(x1, y1, x2, y2, radius=1):
    """
    Draws two points in dice based on the given coordinates and radius

    :param x1:      x-coordinate of the first dot
    :param y1:      y-coordinate of the first dot
    :param x2:      x-coordinate of the second dot
    :param y2:      y-coordinate of the second dot
    :param radius:  radius of the dots to be drawn

    :return: None
    """
    draw_one_dot(x1, y1, radius)
    draw_one_dot(x2, y2, radius)


def draw_dice(dice_number, side=150, radius=3):
    """
    Draws dice based on the dice_number number

    :param dice_number: the number to be shown on dice

    :return: None
    """
    # Bring back to draw dice
    t.goto(-75, 0)

    if 1 <= dice_number <= 6:
        draw_outline(side)
    if dice_number == 1:
        draw_one_dot(side / 2, side / 2, radius=radius)
    elif dice_number == 2:
        draw_two_dots(side / 4, side / 4, 3 * side / 4, 3 * side / 4, radius=radius)
    elif dice_number == 3:
        draw_one_dot(side / 2, side / 2, radius=radius)
        draw_two_dots(side / 4, side / 4, 3 * side / 4, 3 * side / 4, radius=radius)
    elif dice_number == 4:
        draw_two_dots(side / 4, side / 4, 3 * side / 4, 3 * side / 4, radius=radius)
        draw_two_dots(side / 4, 3 * side / 4, 3 * side / 4, side / 4, radius=radius)
    elif dice_number == 5:
        draw_one_dot(side / 2, side / 2, radius=radius)
        draw_two_dots(side / 4, side / 4, 3 * side / 4, 3 * side / 4, radius=radius)
        draw_two_dots(side / 4, 3 * side / 4, 3 * side / 4, side / 4, radius=radius)
    elif dice_number == 6:
        draw_two_dots(side / 4, side / 2, 3 * side / 4, side / 2, radius=radius)
        draw_two_dots(side / 4, 3 * side / 4, 3 * side / 4, side / 4, radius=radius)
        draw_two_dots(side / 4, side / 4, 3 * side / 4, 3 * side / 4, radius=radius)


def top_bar(keeper, dice):
    """
    Creates a top bar and displays the scores of both player who are in the game

    :param keeper: the score keeper object with its relevant information about player and score

    :return:       None

    :pre:  pos (0  , 0), heading (north), pen up
    :post: pos (-75, 0), heading (east) , pen down
    """
    # Create top bar
    t.penup()
    t.left(90)
    t.fd(400)
    t.left(90)
    t.fd(1980 / 2)

    t.pendown()
    t.left(180)
    t.fd(1980)

    t.penup()
    t.left(180)
    t.fd(1.75 * 1980 / 2)
    t.right(90)

    # When there's a dice roll equals to 1, it prompts the players that there's going to be a change
    if dice != 1:
        t.color("blue")
        t.write(f"Currently playing: Player  {keeper.player}", font=("Arial", 10, "normal"))
        t.color("black")
    if dice == 1:
        t.color("blue")
        t.write(f"Player changed from Player {1 - keeper.player} to Player {keeper.player}"
                f"\nNow Playing - Player "
                f"{keeper.player}", font=("Arial", 10, "normal"))
        t.color("black")
    t.fd(40)
    t.left(90)
    t.write(f"Player 0: {keeper.score[0]}", font=("Arial", 30, "normal"))
    t.back(1980 / 1.6)
    t.write(f"Player 1: {keeper.score[1]}", font=("Arial", 30, "normal"))

    # Bring back to center
    t.goto(-75, 0)
    t.left(180)


def game_over(player, points):
    """
    Creates a Game over screen  with the winner and their points

    :@param player:   determines which of two players is playing
    :@param points:   points of the current player
    :@return:   None

    :pre:  pos (-20, 20), heading (west), pen down
    :post: pos (0  , 0) , heading (east), pen up
    """

    t.clear()
    t.goto(-20, 20)
    t.write("GAME OVER!")
    t.goto(-20, 10)
    t.write(f"Player {player} won! with {points} points")

    t.penup()
    t.goto(0, 0)
    time.sleep(10)

    t.Screen().bye()  # Kills the turtle window


def show_points(keeper):
    """
    Shows the total points at each turn

    :param keeper:  object holding all the information regarding player, scores, and points

    :return:        None
    """
    t.goto(-50, -150)
    t.write(f"Turn total: {keeper.points}", font=("Arial", 15, "normal"))


def game_logic(x, y):
    """
    This function accepts the onscreen click coordinates and runs other modules accordingly
    :param:     x,y     Coordinates of clicks
    :return:    None

    :pre:   Clears the turtle window and stores a random number
    """

    if (-75 < x < 75 and 0 < y < 150) or (-60 < x < 65 and -75 < y < -25):
        t.clear()
        dice_num = random.randint(1, 6)
        draw_dice(dice_num, SIDE, RADIUS)
        hold_button()

    if -60 < x < 65 and -75 < y < -25 and dice_num != 1:
        keeper.switch_player()
        keeper.points = dice_num
    elif dice_num == 1:
        keeper.points = 0
        keeper.switch_player()
    else:
        keeper.add_points(dice_num)

    top_bar(keeper, dice_num)

    if keeper.score[0] >= MAX_SCORE:
        game_over(0, keeper.score[0])
    if keeper.score[1] >= MAX_SCORE:
        game_over(1, keeper.score[1])

    show_points(keeper)


def hold_button():
    """
    This function create a hold button for turtle game

    :return:None

    :pre:  pos (-50,-75), heading (west), pen down
    :post: pos ( 0 , 0) , heading (east), pen up
    """
    t.goto(-50, -75)
    t.write("HOLD", font=("Arial", 30, "normal"))
    t.goto(-60, -75)
    t.pendown()
    for _ in range(2):
        t.fd(125)
        t.left(90)
        t.fd(50)
        t.left(90)
    t.penup()
    t.goto(0, 0)


def main():
    """
    Main function
    """
    init(0, "PIG DICE")
    t.write("Click HERE to start the game!")
    t.right(90)
    t.forward(30)
    t.left(90)
    t.write("\n.......\nClick on Hold to hold and \nClick anywhere to roll die")
    t.onscreenclick(game_logic, btn=1, add=None)
    t.mainloop()
    t.clear()


if __name__ == '__main__':
    main()
