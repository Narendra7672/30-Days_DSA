import heapq

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    g = [[] for _ in range(n + 1)]
    for u, v, w in times:
        g[u].append((v, w))
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    pq = [(0, k)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    max_time = max(dist[1:])
    return max_time if max_time != float('inf') else -1
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  # Output: 2
