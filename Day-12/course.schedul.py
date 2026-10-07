from collections import deque

def can_finish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1
    queue = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
    completed = 0
    while queue:
        current = queue.popleft()
        completed += 1
        for next_course in graph[current]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    return completed == numCourses
numCourses = 2
prerequisites = [[1, 0]]

print(can_finish(numCourses, prerequisites))