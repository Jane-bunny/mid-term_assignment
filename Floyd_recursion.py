# Write the Floyd-Warshall Algorithm with recursion

# Define the variable INF, which represents the opposite nodes and nodes
# which are not in the path direction.
INF = 10**9

# Define the function which finds the shortest path from input graph.
def floyd_warshall_recursive(graph, number_nodes):
    """
    Finds the shortest path between all pairs of nodes in a graph using\
    Floyd-Warshall algorithm with recursion.

    Args:
        graph (list): A matrix representation of the graph. INF stands for the opposite node
        and the node which is not in the path direction.
        number_nodes (int): The number of nodes in the graph. 
    Returns: 
    A matrix of the shortest distances between all pairs of nodes.
    """
    # Initialise a 2D matrix which the distances (Shortest) will be populated later.
    dist = [[INF for i in range(number_nodes)] for j in range(number_nodes)]

    # Define the shortest distance finding founction.
    def find_shortest_distance(i, j, k):
        """
        Recursive helper function to find the shortest distance between i and j
        through intermediate nodes.

        Args:
        i (int): Starting node.
        j (int): Ending node.
        k (int): Number of intermediate nodes to consider.

        Returns:
        Shortest distance between i and j through k intermediate nodes.
        """ 
        # Base case: first consider the distance between the nodes which
        # connected with each other, meaning no intermediate nodes.
        # k is the number of the intermediate nodes.
        if k == -1:
            return graph[i][j]
        # Recursive case: find the shortest distance between i and j \
        #through intermediate nodes.
        else:
            return min(find_shortest_distance(i, j, k - 1),
                      (find_shortest_distance(i, k, k - 1) +
                       find_shortest_distance(k, j, k - 1)))

    # Apply the shortest distance finding function for all pairs of nodes.
    # Base case: shortest distance is one node with itself.
    for i in range(number_nodes):
        dist[i][i] = 0

    # Compute shortest distances between all pairs of nodes
    for i in range(number_nodes):
        for j in range(number_nodes):
            dist[i][j] = find_shortest_distance(i, j, number_nodes - 1)
    return dist

# Call the function
# Define the weighted adjacency matrix of the graph
graph = [
            [0, 10, 10**9, 5, 10**9],
            [10**9, 0, 10**9, 10, 10**9],
            [1, 10**9, 0, 10**9, 10],
            [10**9, 2, 10**9, 0, 10**9],
            [10**9, 3, 10**9, 10, 0]
        ]
number_nodes = len(graph)
dist = floyd_warshall_recursive(graph, number_nodes)

# Print the matrix
for i in range(number_nodes):
    for j in range(number_nodes):
        # Use end='' to prevent the print function from adding a newline
        print(dist[i][j], end=' ')
    # After printing all the elements in a row, print a newline to move to the next row
    print()
# This code is provided by Jane. Z.