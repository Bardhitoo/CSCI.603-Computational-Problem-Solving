from graph import Graph

ROCK = "*"


def read_maze(file_name: str):
    """
    Reads the  the top most value possible value where a person at coordinate x,y(row ,column)
    can go

    :param file_name:       the name of the file which the program reads the input from

    :return (maze, data):   tuple packing for the matrix of input from file, and the relevant data regarding the file
    """
    maze = []
    with open(file_name) as f:
        lines = f.readlines()

        for line in lines:
            maze.append((line.strip("\n")).split(' '))

    # height, width, and escape row
    data = eval(maze[0][0]), eval(maze[0][1]), eval(maze[0][2])
    maze = maze[1:]

    return maze, data


def is_up(row, col, maze):
    """
    Finds the top most value possible value where a person at coordinate x,y(row ,column)
    can go
    
    :param row:     row coordinate of the node in the graph
    :param col:     column coordinate of the node in the graph
    :param maze:    the matrix of the maze with the data

    :return:    
    None if top movement is not possible
    Tuple(y,x) - (column no, row no) is top movement is possible
    """

    check_maze = maze[:row]  # Sliced Maze to check

    if len(check_maze) == 0:  # if the sliced list is empty
        return None
    if len(check_maze) == 1:  # if sliced list is 1d
        if check_maze[0][col] != ROCK:
            return col, row - 1
    else:
        len_of_2d = len(check_maze)  # len_of_2d -> num_s
        len_of_1d = len(check_maze[0])  # len_of_1d -> num_cols
        x = None  # Final row coord
        y = None  # Final column coord
        for rows in range(len_of_2d - 1, -1, -1):
            if check_maze[rows][col] != ROCK:
                x, y = rows, col
            if check_maze[rows][col] == ROCK:
                if x is None and y is None:
                    return None
                else:
                    return y, x

        return y, x


def is_down(row, col, maze):
    """
    Finds the down most value possible value where a person at coordinate x,y(row ,column)
    can go

    :param row:     row coordinate of the node in the graph
    :param col:     column coordinate of the node in the graph
    :param maze:    the matrix of the maze with the data

    :return:
    None if top movement is not possible
    Tuple(y,x) - (column no, row no) is top movement is possible
    """

    check_maze = maze[row + 1:]  # Sliced Maze to check

    if len(check_maze) == 0:
        return None
    if len(check_maze) == 1:
        if check_maze[0][col] != ROCK:
            return col, row + 1

    else:
        len_of_2d = len(check_maze)
        len_of_1d = len(check_maze[0])
        x = None
        y = None
        for rows in range(0, len_of_2d):
            if check_maze[rows][col] != ROCK:
                x, y = rows + row + 1, col
            if check_maze[rows][col] == ROCK:
                if x is None and y is None:
                    return None
                else:
                    return y, x

        return y, x


def is_right(row, col, maze):
    """
    Finds the right-most value possible value where a person at coordinate x,y(row ,column)
    can go

    :param row:     row coordinate of the node in the graph
    :param col:     column coordinate of the node in the graph
    :param maze:    the matrix of the maze with the data

    :return:
    None if top movement is not possible
    Tuple(y,x) - (column no, row no) is top movement is possible
    """

    check_maze = maze[row]
    right = None
    for items in range(len(check_maze)):

        if items > col:
            if check_maze[items] == ".":
                right = items
            if check_maze[items] == ROCK:
                break

    if right is not None:
        return right, row
    else:
        return None


def is_left(row, col, maze):
    """
    Finds the left-most value possible value where a person at coordinate x,y(row ,column)
    can go

    :param row:     row coordinate of the node in the graph
    :param col:     column coordinate of the node in the graph
    :param maze:    the matrix of the maze with the data

    :return:
    None if top movement is not possible
    Tuple(y,x) - (column no, row no) is top movement is possible
    """

    check_maze = maze[row]
    left = None
    for items in range(len(check_maze) - 1, -1, -1):

        if items < col:
            if check_maze[items] == ".":
                left = items
            if check_maze[items] == ROCK:
                break

    if left is not None:
        return left, row
    else:
        return None


def make_graph(paths):
    """
    Makes graph using the adjacency list of vertices
    :param paths:            Adjacency dict of the graph

    :return ice_pond_graph:  Graph of the vertices of the ice pond

    """
    ice_pond_graph = Graph()
    for nodes, neighbors in paths.items():
        for neighbor in neighbors:
            if neighbor is not None:
                # this automatically creates a new vertex if not already present
                ice_pond_graph.addEdge(nodes, neighbor)

    return ice_pond_graph


def find_shortest_path(start, end):
    """
    Find the shortest path, if one exists, between a start and end vertex
    :param start (Vertex): the start vertex
    :param end (Vertex): the destination vertex

    :return: A list of Vertex objects from start to end, if a path exists,
             otherwise None
    """
    # Using a queue as the dispenser type will result in a breadth first
    # search
    queue = []
    queue.append(start)  # prime the queue with the start vertex

    # The predecessor dictionary maps the current Vertex object to its
    # immediate predecessor.  This collection serves as both a visited
    # construct, as well as a way to find the path
    predecessors = {}
    predecessors[start] = None  # add the start vertex with no predecessor

    # Loop until either the queue is empty, or the end vertex is encountered
    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getConnections():
            if neighbor not in predecessors:  # if neighbor unvisited
                predecessors[neighbor] = current  # map neighbor to current
                queue.append(neighbor)  # enqueue the neighbor

    # If the end vertex is in predecessors a path was found
    if end in predecessors:
        path = []
        current = end
        while current != start:  # loop backwards from end to start
            path.insert(0, current)  # prepend current to the path list
            current = predecessors[current]  # move to the predecessor
        path.insert(0, start)
        return path
    else:
        return None


def create_and_populate_graph(maze, col_length, escape_row):
    """
    Creates and populates the graph with the relevant information from the maze

    :param maze:    Matrix of the maze

    :return:        Graph of the vertices of the ice pond
    """
    paths = {}

    for i in range(len(maze)):
        for j in range(len(maze[1])):
            if maze[i][j] != ROCK:
                paths[(j, i)] = [is_up(i, j, maze), is_down(i, j, maze), is_right(i, j, maze), is_left(i, j, maze)]
            if col_length - 1 == j and escape_row == i and maze[col_length - 1][escape_row] != ROCK:
                paths[(j, i)] = [(j, i)]
    return make_graph(paths)


def find_all_possible_paths(ice_pond_graph, maze_width, escape_row):
    """
    Utilizes breadth-first search to find the shortest path out of the maze for all possible vertices in the graph

    :param ice_pond_graph:    Graph of maze
    :param maze_width:        Width of maze
    :param escape_row:        Row in which escape occures

    :return steps:            Dictionary for number_of_steps_to_exit and initial vertex
    """
    steps = dict()
    no_paths = []
    for vertex in ice_pond_graph.getVertices():
        if vertex == (maze_width - 1, escape_row):
            if "1" in steps.keys():
                steps["1"].append(vertex)
            else:
                steps["1"] = [vertex]
            continue

        temp = find_shortest_path(ice_pond_graph.getVertex(vertex),
                                  ice_pond_graph.getVertex((maze_width - 1, escape_row)))
        if temp is None:
            no_paths.append(vertex)
            continue

        l = [v for v in temp]
        l.pop(0)
        number_of_steps_to_exit = len(l)

        if str(number_of_steps_to_exit) not in steps.keys():
            steps[str(number_of_steps_to_exit)] = [vertex]
        else:
            steps[str(number_of_steps_to_exit)].append(vertex)

    return steps, no_paths


def beautify(steps_for_all_possible_paths):
    """
    Prepares a more user-friendly output

    :param steps_for_all_possible_paths:    Dictionary for number_of_steps_to_exit and initial vertex
    """
    sorted_steps = sorted(steps_for_all_possible_paths.keys())

    for step in sorted_steps:
        print(f"{step}: {steps_for_all_possible_paths[step]}")


def main():
    """
    Main function
    """
    maze, data = read_maze("test2.txt")
    row_length, col_length, escape_row = data

    ice_pond_graph = create_and_populate_graph(maze, col_length, escape_row)

    steps_for_all_possible_paths, no_paths = find_all_possible_paths(ice_pond_graph, col_length, escape_row)

    if len(steps_for_all_possible_paths.keys()) == 0:
        print("No possible way to escape! Double-check your input.")
        print(no_paths)

    beautify(steps_for_all_possible_paths)


if __name__ == "__main__":
    main()
