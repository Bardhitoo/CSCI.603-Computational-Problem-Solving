import math
import turtle

def draw_side1(n: int):
    turtle.forward(n)

def draw_side2(n: int):
    draw_side1(n/3)
    turtle.left(60)
    draw_side1(n/3)
    turtle.right(120)
    draw_side1(n/3)
    turtle.left(60)
    draw_side1(n/3)

def draw_side(len: int, level: int, angle: int):
    acc_len = 0
    if level == 1:
        turtle.forward(len)
        return acc_len + len
    else:
        acc_len += draw_side(len/3, level-1, angle)
        turtle.left(angle)
        acc_len += draw_side(len / ((math.cos(math.radians(angle))*6)), level-1, angle)
        turtle.right(2*angle)
        acc_len += draw_side(len / ((math.cos(math.radians(angle))*6)), level-1, angle)
        turtle.left(angle)
        acc_len += draw_side(len/3, level-1, angle)
    return acc_len

turtle.penup()
turtle.speed(0)
turtle.hideturtle()
turtle.forward(-150)
turtle.pendown()
totalLength = draw_side(150, 2, 80)
turtle.exitonclick()
print(totalLength)