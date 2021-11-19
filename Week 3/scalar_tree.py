import turtle as t


def draw_tree(length, segment):
    if segment == 0:
        pass
    else:
        t.fd(length)
        t.left(45)
        draw_tree(length / 1.5, segment - 1)
        t.right(90)
        draw_tree(length / 1.5, segment - 1)
        t.left(45)
        t.fd(-length)


def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial_rec_tail(n, a):
    if n == 1:
        return a
    else:
        return factorial_rec_tail(n - 1, a * n)


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fun(n):
    if n == 0:
        return 0
    else:
        return fun(n-1) + 2*n - 1


def minCoins(a):
    if a == 0:
        return 0
    elif 0 < a and a < 5:
        return 1 + minCoins(a - 1)
    elif 4 < a and a < 10:
        return 1 + minCoins(a - 5)
    elif 9 < a and a < 25:
        return 1 + minCoins(a - 10)
    else:
        return 1 + minCoins(a - 25)

print(minCoins(65))
