# Minimum Cost to Cut a Stick:
def minCost(n: int, cuts: list[int]) -> int:
    cuts = sorted(cuts + [0, n])
    m = len(cuts)
    dp = [[0] * m for _ in range(m)]
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + (
                cuts[j] - cuts[i]
            )
    return dp[0][m - 1]


n = 7
cuts = [1, 3, 4, 5]
print(minCost(n, cuts))
