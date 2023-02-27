import time
from Floyd_iterative import floydWarshall

INF = 99999

if __name__ == "__main__":
    graph = [
        [0, INF, INF, INF, INF],
        [INF, 0, 4, 1, 4],
        [INF, 3, 0, INF, INF],
        [INF, INF, INF, 0, 2],
        [INF, INF, INF, INF, 0]
    ]

start_time = time.time()
result = floydWarshall(graph)
end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")