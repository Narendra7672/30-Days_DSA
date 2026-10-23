# Maximum Equal Frequency:
from collections import Counter


def maxEqualFreq(nums):
    count = Counter()
    freq = Counter()
    max_f = 0
    ans = 0
    for i, num in enumerate(nums):
        c = count[num]
        if c > 0:
            freq[c] -= 1
        count[num] += 1
        c = count[num]
        freq[c] += 1
        max_f = max(max_f, c)
        if max_f == 1:
            ans = i + 1
        elif freq[max_f] * max_f == i:
            ans = i + 1
        elif (freq[max_f - 1] + 1) * (max_f - 1) == i:
            ans = i + 1
    return ans


nums = [2, 2, 1, 1, 5, 3, 3, 5]
print(maxEqualFreq(nums))
