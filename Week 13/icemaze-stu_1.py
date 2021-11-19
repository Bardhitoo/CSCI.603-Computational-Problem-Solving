length, width, exit = 5, 5, 1  # TODO: read args

from graph import Graph


def read_maze():
    maze = []
    # maze.append(["*" for _ in range(width + 2)])
    with open("maze_1.txt") as f:
        lines = f.readlines()

        for line in lines:
            maze.append((line.strip("\n")).split(' '))

    data = maze[0]
    maze = maze[1:]

    return maze, data


def is_next_rock(maze: list, coorX: int, coorY: int, direction: int) -> bool:
    """
    Checks to see if the next location a rock

    :param direction: 0 for x-axis, 1 for y-axis
    """


def is_up(i, j, maze):
    """
    Finds the top most value possible value where a person at coordinate x,y(row ,column)
    can go

    :param variable: i,j - row number and column number of a node whose top most movement
    needs to be found

    :return:    
    None if top movement is not possible
    Tuple(y,x) - (column no, row no) is top movement is possible

    """

    check_maze = maze[:i]  # Sliced Maze to check

    if len(check_maze) == 0:  # if the sliced list is empty
        return None
    if len(check_maze) == 1:  # if sliced list is 1d
        if (check_maze[0][j] != "*"):
            return (j, i - 1)

    else:
        len_of_2d = len(check_maze)
        len_of_1d = len(check_maze[0])
        x = None  # Final row coord
        y = None  # Final column coord
        for rows in range(len_of_2d - 1, -1, -1):
            for columns in range(0, len_of_1d):
                if (columns == j and check_maze[rows][columns] != "*"):
                    x, y = rows, columns
                if (columns == j and check_maze[rows][columns] == "*"):
                    if (x == None and y == None):
                        return None
                    else:
                        return (y, x)

        return (y, x)


def is_down(i, j, maze):
    """
    Finds the bottom most value possible value where a person at coordinate x,y(row ,column)
    can be

    :param 
    int i,j - row number and column number of a node whose botton most movement
    needs to be found
    2d list : maze - Actual maze matrix

    :return:    
    None if bottom movement is not possible
    Tuple(y,x) - (column no, row no) if bottom movement is possible
    """

    check_maze = maze[i + 1:]  # Sliced Maze to check

    if len(check_maze) == 0:
        return None
    if len(check_maze) == 1:
        # print(len(check_maze))
        # print(check_maze[1])
        if (check_maze[0][j] != "*"):
            return (j, i + 1)

    else:
        len_of_2d = len(check_maze)
        len_of_1d = len(check_maze[0])
        x = None
        y = None
        for rows in range(0, len_of_2d):
            for columns in range(0, len_of_1d):
                if (columns == j and check_maze[rows][columns] != "*"):
                    x, y = rows + i + 1, columns
                if (columns == j and check_maze[rows][columns] == "*"):
                    if (x == None and y == None):
                        return None
                    else:
                        return (y, x)

        return (y, x)


def is_right(i, j, maze):
    """
    Finds the right most value possible value where a person at coordinate x,y(row ,column)
    can be

    :param 
    int: i,j - row number and column number of a node whose right most movement
    needs to be found
    2d list : maze - Actual maze matrix

    :return:    
    None if right movement is not possible
    Tuple(y,x) - (column no, row no) if right movement is possible
    """
    check_maze = maze[i]
    right = None
    for items in range(len(check_maze)):

        if (items > j):
            if (check_maze[items] == "."):
                right = items
            if (check_maze[items] == "*"):
                break

    if right != None:
        return (right, i)
    else:
        return None


def is_left(i, j, maze):
    """
    Finds the left most value possible value where a person at coordinate x,y(row ,column)
    can be

    :param 
    int: i,j - row number and column number of a node whose left most movement
    needs to be found
    2d list : maze - Actual maze matrix

    :return:    
    None if left movement is not possible
    Tuple(y,x) - (column no, row no) if left movement is possible
    """
    check_maze = maze[i]
    left = None
    for items in range(len(check_maze) - 1, -1, -1):

        if (items < j):
            if (check_maze[items] == "."):
                left = items
            if (check_maze[items] == "*"):
                break

    if left != None:
        return (left, i)
    else:
        return None


def make_graph(paths):
    """
    Makes graph using the adjacency list of vertices
    :param
    dict paths -    adjacency dict of the graph

    :return
    Graph ice_pond_graph -  Graph of the vertices of the ice pond

    """
    ice_pond_graph = Graph()
    for nodes, neighbors in paths.items():
        for neighbor in neighbors:
            if (neighbor != None):
                # this automatically creates a new vertices if not already present
                ice_pond_graph.addEdge(nodes, neighbor)

    return ice_pond_graph


def main():
    maze, user_data = read_maze()

    paths = {}
    print(maze[1])

    for i in range(len(maze)):
        for j in range(len(maze[1])):
            if (maze[i][j] != "*"):
                paths[(j, i)] = [is_up(i, j, maze), is_down(i, j, maze), is_right(i, j, maze), is_left(i, j, maze)]

    print(paths)

    ice_pond_graph = make_graph(paths)
    for node in ice_pond_graph:
        print(node)


if __name__ == "__main__":
    main()
