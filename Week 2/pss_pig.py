import turtle as t

    
def init(speed=5):
    """
    Initializes the drawing window

    :param font_size the size of the word

    :pre: position (0,0), heading east, pen down
    :post: position (0,0), heading east, pen up
    :return: None
    """

    t.title("PSS PIG")
    t.penup()
    t.speed(speed)
    t.showturtle()


init()


def draw_outline(x):
    """
    Draws a square in current direction
    :param length: how long the line of T should be.
    :return: none

    :pre: heading right
    :post: heading right

    """
    t.pendown()
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)


def draw_center_dot(x1, y1, radius=1):
    """
    Draws the single dot in center
    :param x1:
    :param y1:
    :param r:
    :return:
    """
    t.penup()
    t.fd(x1+radius)
    t.left(90)
    t.fd(y1+radius)

    t.pendown()
    t.fillcolor('black')
    t.begin_fill()

    t.circle(radius=radius)
    t.end_fill()

    t.penup()
    t.fd(-y1-radius)
    t.right(90)
    t.fd(-x1-radius)


def draw_two_dots(x1,y1, x2, y2, radius=1):
    draw_center_dot(x1, y1, radius)
    draw_center_dot(x2, y2, radius)

SIDE = 150
RADIUS = 3
# pips = 0

pips = 6
# pips = int(input("Please enter the side of the dice:"))
# assert 1 <= pips <= 5, f"Illegal #pips: {pips}"

if 1 <= pips <= 6:
    init(speed=6)
    draw_outline(SIDE)
if pips == 1:
    draw_center_dot(SIDE/2, SIDE/2, radius=RADIUS)
elif pips == 2:
    draw_two_dots(SIDE/4, SIDE/4, 3*SIDE/4, 3*SIDE/4, radius=RADIUS)
elif pips == 3:
    draw_center_dot(SIDE/2, SIDE/2, radius=RADIUS)
    draw_two_dots(SIDE/4, SIDE/4, 3*SIDE/4, 3*SIDE/4, radius=RADIUS)
elif pips == 4:
    draw_two_dots(SIDE/4, SIDE/4, 3*SIDE/4, 3*SIDE/4, radius=RADIUS)
    draw_two_dots(SIDE/4, 3*SIDE/4, 3*SIDE/4,  SIDE/4, radius=RADIUS)
elif pips == 5:
    draw_center_dot(SIDE/2, SIDE/2, radius=RADIUS)
    draw_two_dots(SIDE/4, SIDE/4, 3*SIDE/4, 3*SIDE/4, radius=RADIUS)
    draw_two_dots(SIDE/4, 3*SIDE/4, 3*SIDE/4,  SIDE/4, radius=RADIUS)
elif pips == 6:
    draw_two_dots(SIDE/4, 3*SIDE/4, 3*SIDE/4, 3*SIDE/4, radius=RADIUS)
    draw_two_dots(SIDE/4, SIDE/2, 3*SIDE/4,  SIDE/2, radius=RADIUS)
    draw_two_dots(SIDE/4, SIDE/4, 3*SIDE/4,  SIDE/4, radius=RADIUS)

t.mainloop()
