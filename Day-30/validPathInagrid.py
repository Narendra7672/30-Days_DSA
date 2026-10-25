# Minimum Cost to Make at Least One Valid Path in a Grid:
from collections import deque

def minCost(grid): 
    m, n = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[float("inf")] * n for _ in range(m)]
    dist[0][0] = 0
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        if r == m - 1 and c == n - 1:
            return dist[r][c]
        for i, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                cost = 0 if grid[r][c] == i + 1 else 1
                if dist[r][c] + cost < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + cost
                    if cost == 0:
                        q.appendleft((nr, nc))
                    else:
                        q.append((nr, nc))
    return dist[m - 1][n - 1]
grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
print(minCost(grid))
