from Floyd_recursion import floyd_warshall_recursive
import unittest

INF = 10**9

class TestFloydWarshallRecursive(unittest.TestCase):
    
    # Case 1, test with 4 nodes
    def test_floyd_warshall_recursive_4_nodes(self):
        # Both versions can be tested, with INF or 10**9 as INF
        #graph = [
            #[0, 5, 10**9, 10],
            #[10**9, 0, 3, 10**9],
            #[10**9, 10**9, 0, 1],
            #[10**9, 10**9, 10**9, 0]
        #]
        graph = [
            [0, 2, 5, INF],
            [INF, 0, 7, 3],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        number_nodes = 4
        expected = [
            [0, 2, 5, 5],
            [10**9, 0, 7, 3],
            [10**9, 10**9, 0, 1],
            [10**9, 10**9, 10**9, 0]
        ]
        self.assertEqual(floyd_warshall_recursive(graph, number_nodes), expected)

    # Case 2, test with 5 nodes.
    def test_floyd_warshall_recursive_5_nodes(self):
        graph = [
            [0, 10, 10**9, 5, 10**9],
            [10**9, 0, 10**9, 10, 10**9],
            [1, 10**9, 0, 10**9, 10],
            [10**9, 2, 10**9, 0, 10**9],
            [10**9, 3, 10**9, 10, 0]
        ]
        number_nodes = 5
        expected =[
            [0, 7, 1000000000, 5, 1000000000],
            [1000000000, 0, 1000000000, 10, 1000000000],
            [1, 8, 0, 6, 10],
            [1000000000, 2, 1000000000, 0, 1000000000],
            [1000000000, 3, 1000000000, 10, 0]
        ] 
  
        self.assertEqual(floyd_warshall_recursive(graph, number_nodes), expected)

if __name__ == '__main__':
    unittest.main()