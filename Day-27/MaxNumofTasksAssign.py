# Maximum Number of Tasks You Can Assign:
from collections import deque
def maxTaskAssign(
    tasks: list[int], workers: list[int], pills: int, strength: int
) -> int:
    tasks.sort()
    workers.sort()
    n, m = len(tasks), len(workers)

    def check(k: int) -> bool:
        pills_left = pills
        queue = deque()
        task_idx = 0
        for worker_idx in range(m - k, m):
            while (
                task_idx < k
                and tasks[task_idx] <= workers[worker_idx] + strength
            ):
                queue.append(tasks[task_idx])
                task_idx += 1
            if not queue:
                return False
            if queue[0] <= workers[worker_idx]:
                queue.popleft()
            elif pills_left > 0:
                pills_left -= 1
                queue.pop()
            else:
                return False
        return True

    left, right = 0, min(n, m)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
tasks = [3, 2, 1]
workers = [0, 3, 3]
pills = 1
strength = 1
print(maxTaskAssign(tasks, workers, pills, strength))
