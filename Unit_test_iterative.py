from Floyd_iterative import floydWarshall
import unittest

INF = 99999

# Code to be tested
def floydWarshall(graph):
    """This function return the dist, because original code only print the dist.\
        when we run unit test, we need to compare the dist value, check if expected output\
        from this function is right. 

    Args:
        graph (list): A matrix representation of the graph. INF stands for the opposite nodes
        and the nodes which are not in the path direction.

    Returns:
        A matrix of the shortest distances between all pairs of nodes.
    """
    # Implementation of floydWarshall function
    V = (len(graph))
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Unit test for floydWarshall function with 4-node graph
class TestFloydWarshall(unittest.TestCase):
    
    # Test case 1, shortest path for 4 nodes.
    def test_shortest_paths_4_nodes(self):
        graph = [
            [0, 2, 5, INF],
            [INF, 0, 7, 3],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        expected = [
            [0, 2, 5, 5],
            [INF, 0, 7, 3],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        result = floydWarshall(graph)
        self.assertEqual(expected, result)

    # Test case 2, shortest path for 5 nodes.
    def test_shortest_paths_5_nodes(self):
        
        graph = [
            [0, INF, INF, INF, INF],
            [INF, 0, 4, 1, 4],
            [INF, 3, 0, INF, INF],
            [INF, INF, INF, 0, 2],
            [INF, INF, INF, INF, 0]
        ]
        expected =  [
            [0, INF, INF, INF, INF],
            [INF, 0, 4, 1, 3],
            [INF, 3, 0, 4, 6],
            [INF, INF, INF, 0, 2],
            [INF, INF, INF, INF, 0]
        ]

        result = floydWarshall(graph)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()