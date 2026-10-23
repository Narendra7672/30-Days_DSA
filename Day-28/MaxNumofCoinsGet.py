# Maximum Number of Coins You Can Get:
def maxCoins(piles):
    piles.sort()
    ans = 0
    n = len(piles)
    for i in range(n // 3, n, 2):
        ans += piles[i]
    return ans
piles = [2, 4, 1, 2, 7, 8]
print(maxCoins(piles))
