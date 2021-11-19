ROCK = "*"


def read_maze():
    maze = []
    # maze.append([ROCK for _ in range(width + 2)])
    with open("maze_1.txt") as f:
        lines = f.readlines()

        for line in lines:
            maze.append((line.strip("\n")).split(' '))
    data = eval(maze[0][0]), eval(maze[0][1]), eval(maze[0][2])
    maze = maze[1:]

    return maze, data


def is_up(i, j, maze):
    check_maze = maze[:i]

    if len(check_maze) == 0:
        return None
    if len(check_maze) == 1:
        # print(len(check_maze))
        # print(check_maze[1])
        if check_maze[0][j] != ROCK:
            return i - 1, j

    else:
        l1 = len(check_maze)
        l2 = len(check_maze[0])
        x = None
        y = None
        for i1 in range(l1 - 1, -1, -1):
            for j1 in range(0, l2):
                if j1 == j and check_maze[i1][j1] != ROCK:
                    x, y = i1, j1
                if j1 == j and check_maze[i1][j1] == ROCK:
                    if x is None and y is None:
                        return None
                    else:
                        return (x, y)

        return (x, y)


def is_down(i, j, maze):
    check_maze = maze[i + 1:]

    if len(check_maze) == 0:
        return None
    if len(check_maze) == 1:
        # print(len(check_maze))
        # print(check_maze[1])
        if (check_maze[0][j] != ROCK):
            return (i + 1, j)

    else:
        l1 = len(check_maze)
        l2 = len(check_maze[0])
        x = None
        y = None
        for i1 in range(0, l1):
            for j1 in range(0, l2):
                if (j1 == j and check_maze[i1][j1] != ROCK):
                    x, y = i1 + i + 1, j1
                if (j1 == j and check_maze[i1][j1] == ROCK):
                    if (x == None and y == None):
                        return None
                    else:
                        return (x, y)

        return (x, y)


def is_right(i, j, maze):
    check_maze = maze[i]
    right = None
    for j2 in range(len(check_maze)):

        if (j2 > j):
            if (check_maze[j2] == "."):
                right = j2
            if (check_maze[j2] == ROCK):
                break

    if right != None:
        return (i, right)
    else:
        return None


def is_left(i, j, maze):
    check_maze = maze[i]
    left = None
    for j2 in range(len(check_maze) - 1, -1, -1):

        if (j2 < j):
            if (check_maze[j2] == "."):
                left = j2
            if (check_maze[j2] == ROCK):
                break

    if left != None:
        return (i, left)
    else:
        return None


def main():
    maze, data = read_maze()
    row_length, col_length, escape_row = data
    paths = {}

    for col in range(col_length):
        for row in range(row_length):
            if maze[col][row] != ROCK:
                paths[(col, row)] = [is_up(col, row, maze), is_down(col, row, maze),
                                     is_right(col, row, maze), is_left(col, row, maze)]
                print(f"{col}, {row} - {paths[(col, row)]}")


if __name__ == "__main__":
    main()
