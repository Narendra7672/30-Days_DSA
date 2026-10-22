# Maximum Number of Achievable Transfer Requests:
def maximumRequests(n: int, requests: list[list[int]]) -> int:
    ans = 0
    m = len(requests)
    indegree = [0] * n

    def backtrack(index, count):
        nonlocal ans
        if index == m:
            if all(x == 0 for x in indegree):
                ans = max(ans, count)
            return
        backtrack(index + 1, count)
        u, v = requests[index]
        indegree[u] -= 1
        indegree[v] += 1
        backtrack(index + 1, count + 1)
        indegree[u] += 1
        indegree[v] -= 1

    backtrack(0, 0)
    return ans


n = 5
requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
print(maximumRequests(n, requests))
