from io import StringIO
from Floyd_iterative import printSolution
import unittest

# Unit test for printSolution function
class TestPrintSolution(unittest.TestCase):

    # Test case for 4 nodes graph
    def test_print_solution_4_nodes(self):
        graph = [
            [0, 2, 5, INF],
            [INF, 0, 7, 3],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        expected_output = "Shortest distances between every pair of vertices:\n"\
                          "  0  2  5  5\n"\
                          "INF  0  7  3\n"\
                          "INF INF  0  1\n"\
                          "INF INF INF  0\n"

        # Redirect the output of printSolution to a buffer
        with StringIO() as buffer:
            printSolution(graph, buffer=buffer)
            output = buffer.getvalue()

        # Compare the contents of the buffer with the expected output
        self.assertEqual(expected_output, output)
