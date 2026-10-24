# Minimum Difficulty of a Job Schedule:
def minDifficulty(jobDifficulty, d):
    n = len(jobDifficulty)
    if n < d:
        return -1
    inf = float("inf")
    dp = [[inf] * (d + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, min(d, i) + 1):
            max_diff = 0
            for k in range(i, j - 1, -1):
                max_diff = max(max_diff, jobDifficulty[k - 1])
                if dp[k - 1][j - 1] != inf:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[k - 1][j - 1] + max_diff
                    )
    return dp[n][d]
jobDifficulty = [6, 5, 4, 3, 2, 1]
d = 2
print(minDifficulty(jobDifficulty, d))