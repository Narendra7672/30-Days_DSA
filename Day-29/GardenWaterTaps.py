# Minimum Number of Taps to Open to Water a Garden:
def minTaps(n: int, ranges: list[int]) -> int:
    max_reach =[0] * (n + 1)
    for i, r in enumerate(ranges):
        start = max(0, i - r)
        end = min(n, i + r)
        max_reach[start] = max(max_reach[start], end)
    taps = 0
    curr_end = 0
    next_end = 0
    for i in range(n):
        if i > next_end:
            return -1
        next_end = max(next_end, max_reach[i])
        if i == curr_end:
            taps += 1
            curr_end = next_end
            if curr_end >= n:
                break
    return taps if curr_end >= n else -1
n = 5
ranges = [3, 4, 1, 1, 0, 0]
print(minTaps(n, ranges))
