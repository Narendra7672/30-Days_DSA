# Course Schedule II:
from collections import deque

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr)
        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == numCourses else []
print(findOrder(2, [[1, 0]]))
