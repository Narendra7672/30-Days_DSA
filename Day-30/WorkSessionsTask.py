# Minimum Number of Work Sessions to Finish the Tasks;
def minSessions(tasks, sessionTime):
    n = len(tasks)
    dp = [(float("inf"), 0)] * (1 << n)
    dp[0] = (1,0)

    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                sessions, rem = dp[prev_mask]

                if rem >= tasks[i]:
                    new_state = (sessions, rem - tasks[i])
                else:
                    new_state = (sessions + 1, sessionTime - tasks[i])

                if new_state < dp[mask]:
                    dp[mask] = new_state

    return dp[(1 << n) - 1]
tasks = [1, 2, 3]
sessionTime = 3

print(minSessions(tasks, sessionTime))
    