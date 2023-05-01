import unittest
import timeit


class WarshallUnitTests(unittest.TestCase):

    def test_input(self):
        """
        This test tests whether there are any mistakes in the formatting of graph information.
        Especially useful for bigger graphs where it's more likely for mistakes to be made in
        manual entry.
        :return: True or False depending on whether values are equal, failure if False.
        """
        control_var = len(input_graph[0])
        for i in input_graph:
            self.assertEqual(len(i), control_var)

    def test_output(self):
        """
        Tests the overall output of the application when given an expected result. Only needs to
        be used once after editing algorithm.
        :return:
        """
        self.assertEqual(expected_result, distance_matrix, 'Result was not what was expected.')


NO_PATH = float('inf')

# Example graph for input.
input_graph = [[0, 5, NO_PATH, 10],
               [NO_PATH, 0, 3, NO_PATH],
               [NO_PATH, NO_PATH, 0, 1],
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

# Expected Result
expected_result = [[0, 5, 8, 9],
                   [NO_PATH, 0, 3, 4],
                   [NO_PATH, NO_PATH, 0, 1],
                   [NO_PATH, NO_PATH, NO_PATH, 0]]


def floyd_warshall(graph):
    """
    A function for working out the shortest path between two points on a given graph.
    :param graph:
    :return: A matrix of all pairs' shortest possible path
    """
    # Define the number of vertices in the graph before applying to function.
    # Define empty memo for memoization.
    num_of_vertices = len(graph)
    memo = {}

    def floyd_warshall_rec(i, j, k, n):
        """
        Recursive part of the algorithm, takes points I and J and intermediate K to figure
        out the shortest possible path, recursively adding 1 to k up to the maximum number of
        vertices.
        :param i: Initial starting point.
        :param j: End position.
        :param k: Any intermediate points.
        :param n: Number of vertices in the graph.
        :return: Each iteration returns the shortest possible path from I to J for each possible pair.
        """
        # if intermediate is equal to the number of vertices in the graph, return result.
        # This acts as base case for recursion.
        if k == n:
            return graph[i][j]

        # If points are already in memo, return the memoized path. Avoid redundant calculations.
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        # If intermediate is less than the total number of vertices, return min distance
        # taking into account paths through k and those not. Store calculations to memo to
        # reduce overhead on performance.
        memo[(i, j, k)] = min(floyd_warshall_rec(i, j, k + 1, n),
                              floyd_warshall_rec(i, k, k + 1, n) +
                              floyd_warshall_rec(k, j, k + 1, n))

        return memo[(i, j, k)]

    # Encapsulating function calls recursive in range of number of vertices.
    calculated_distance_matrix = [[floyd_warshall_rec(i, j, 0, num_of_vertices)
                                   for j in range(num_of_vertices)]
                                  for i in range(num_of_vertices)]

    return calculated_distance_matrix


# Calculate the shortest distance matrix using Floyd-Warshall
distance_matrix = floyd_warshall(second_example)

# Print the result splitting by row of distances.
for row in distance_matrix:
    print(row)

# Initializes and runs unittests
if __name__ == "__main__":
    unittest.main()

# Timing function for measuring performance.
print(timeit.timeit(globals=globals()))
