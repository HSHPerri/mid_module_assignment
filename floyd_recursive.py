import unittest
import timeit


class WarshallUnitTests(unittest.TestCase):

    # Test whether a sample input creates the expected output.
    def test_output(self):
        self.assertEqual(expected_result, distance_matrix, 'Result was not what was expected.')


NO_PATH = float('inf')

# Application needs graph information.
# Example graph for input.
input_graph = [[0, 5, NO_PATH, 10],
               [NO_PATH, 0, 3, NO_PATH],
               [NO_PATH, NO_PATH, 0, 1],
               [NO_PATH, NO_PATH, NO_PATH, 0]]

# Second example graph with 9 vertices.
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
    # Define the number of vertices in the graph before applying it to function.
    num_vertices = len(graph)

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
        # If intermediate is greater than the number of vertices in the graph, return result.
        # This acts as base case for recursion.
        if k == n:
            return graph[i][j]

        # If intermediate is less than the total number of vertices, then return the minimum distance
        # taking into account paths through K and those not.
        return min(floyd_warshall_rec(i, j, k + 1, num_vertices),
                   floyd_warshall_rec(i, k, k + 1, num_vertices) + floyd_warshall_rec(k, j, k + 1, num_vertices))

    # Encapsulating function calls recursive in range of the number of vertices.
    calculated_distance_matrix = [[floyd_warshall_rec(i, j, 0, num_vertices)
                                   for j in range(num_vertices)]
                                  for i in range(num_vertices)]
    return calculated_distance_matrix


# Function call - assigning the resulting value to variable.
distance_matrix = floyd_warshall(input_graph)

# Print the result splitting by row of distances.
for row in distance_matrix:
    print(row)

# Run unit tests
if __name__ == "__main__":
    unittest.main()

# Timing function for measuring performance
print(timeit.timeit(globals=globals()))


