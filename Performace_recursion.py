import time
from Floyd_recursion import floyd_warshall_recursive

INF = 10**9

if __name__ == "__main__":
    graph = [
        [0, INF, INF, INF, INF],
        [INF, 0, 4, 1, 4],
        [INF, 3, 0, INF, INF],
        [INF, INF, INF, 0, 2],
        [INF, INF, INF, INF, 0]
    ]
# Define the size of the graph
number_nodes = len(graph)
# Measure the execution time of the function
start_time = time.time()
result = floyd_warshall_recursive(graph, number_nodes)
end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")