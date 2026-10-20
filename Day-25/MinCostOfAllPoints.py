# Minimum Cost to Connect All Points
import heapq
def min_cost_connect_points(points):
    n = len(points)
    visited = [False] * n
    min_heap = [(0, 0)] 
    total_cost = 0
    edges_used = 0
    while edges_used < n:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        edges_used += 1
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(
                    points[u][1] - points[v][1]
                )
                heapq.heappush(min_heap, (dist, v))

    return total_cost

points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(min_cost_connect_points(points))
