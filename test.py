import unittest


INF = 99999
# code to be tested
def floydWarshall(graph):
    # implementation of floydWarshall function
    V = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# unit test for floydWarshall function with 4-node graph
class TestFloydWarshall(unittest.TestCase):
    
    def test_shortest_paths_4_nodes(self):
        graph = [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        expected = [
            [0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        result = floydWarshall(graph)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()