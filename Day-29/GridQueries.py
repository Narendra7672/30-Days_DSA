# Maximum Number of Points from Grid Queries:
import heapq
def maxPoints(grid: list[list[int]], queries: list[int]) -> list[int]:
    m, n = len(grid), len(grid[0])
    indexed_queries = sorted((q, i) for i, q in enumerate(queries))
    answer = [0] * len(queries)
    heap = [(grid[0][0], 0, 0)]
    visited = {(0, 0)}
    points = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for query, idx in indexed_queries:
        while heap and heap[0][0] < query:
            val, r, c = heapq.heappop(heap)
            points += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
        answer[idx] = points
    return answer
grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
print(maxPoints(grid, queries))
