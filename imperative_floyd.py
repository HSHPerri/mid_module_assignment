import timeit
import itertools

NO_PATH = 100
graph = [[0, 7, 14, 20],
         [NO_PATH, 0, 5, 11],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

# Second example
second_example = [[0, 37, 20, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
                  [NO_PATH, 0, NO_PATH, NO_PATH, 13, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
                  [NO_PATH, NO_PATH, 0, 14, NO_PATH, 9, NO_PATH, NO_PATH, NO_PATH],
                  [25, NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH, 10, NO_PATH, NO_PATH],
                  [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0,  8, NO_PATH, 19, NO_PATH],
                  [NO_PATH, 4, NO_PATH, 17, NO_PATH, 0, 12, NO_PATH, 23],
                  [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, 8],
                  [NO_PATH, 40, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH],
                  [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 23, NO_PATH, 10, 0]]

number_vertices = len(graph[0])


def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """

    for intermediate, start_node, end_node \
            in itertools.product(range(number_vertices), range(number_vertices), range(number_vertices)):

        # Assume that if start_node and end_node are the same
        # then distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # Return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node])

    print(distance)


floyd(second_example)

print(timeit.timeit(globals=globals()))
