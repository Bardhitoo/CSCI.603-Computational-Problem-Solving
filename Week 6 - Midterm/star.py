import sys
import math
import turtle as t


def draw_square1(length):
    for _ in range(4):
        t.fd(length)
        t.left(90)


def draw_triangle1(length):
    for _ in range(3):
        t.fd(length)
        t.right(120)


def draw_square2(length):
    draw_square1(length)
    t.penup()
    t.fd(length / 2)
    t.left(45)
    t.pendown()
    draw_square1(math.sqrt(2 * ((length / 2) ** 2)))


def draw_star1(length):
    beta = length / math.sqrt(3)
    draw_square1(length)

    for _ in range(4):
        t.fd((length / 2) - (beta / 2))
        t.right(60)
        t.fd(beta)
        t.left(120)
        t.fd(beta)
        t.right(60)
        t.fd((length / 2) - (beta / 2))
        t.left(90)


def draw_nested_star(length, depth, colors):
    t.color(colors[depth % len(colors)])

    if depth == 0:
        return

    beta = length / math.sqrt(3)
    for _ in range(4):
        t.fd(length)
        t.left(90)

    for _ in range(4):
        t.fd((length / 2) - (beta / 2))
        t.right(60)
        t.fd(beta)
        t.left(2 * 60)
        t.fd(beta)
        t.right(60)
        t.fd((length / 2) - (beta / 2))
        t.left(90)

    t.fd(length / 2)
    t.left(45)
    draw_nested_star(math.sqrt(2 * ((length / 2) ** 2)), depth - 1, colors)


def main():
    if len(sys.argv) != 3:
        exit("Usage: python3 start.py depth length")

    try:
        depth = int(sys.argv[1])
    except:
        exit("Please input a valid <int> for the variable depth")

    try:
        length = float(sys.argv[2])
        # assert length > 0
    except:
        exit("Please input a valid <float> for the variable depth")

    colors = ('red', 'purple', 'orange', 'blue', 'green', 'aqua')
    t.speed(10)
    draw_nested_star(length, depth, colors)
    t.mainloop()


if __name__ == "__main__":
    main()
