# Maximum Sum of 3 Non-Overlapping Subarrays:
def maxSumOfThreeSubarrays(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    window_sums = []
    current_sum = sum(nums[:k])
    window_sums.append(current_sum)
    for i in range(k, n):
        current_sum += nums[i] - nums[i - k]
        window_sums.append(current_sum)
    m = len(window_sums)
    left = [0] * m
    best = 0
    for i in range(m):
        if window_sums[i] > window_sums[best]:
            best = i
        left[i] = best
    right = [0] * m
    best = m - 1
    for i in range(m - 1, -1, -1):
        if window_sums[i] >= window_sums[best]:
            best = i
        right[i] = best
    max_total = float("-inf")
    answer = []
    for mid in range(k, m - k):
        first = left[mid - k]
        third = right[mid + k]
        total = (
            window_sums[first]
            + window_sums[mid]
            + window_sums[third]
        )
        if total > max_total:
            max_total = total
            answer = [first, mid, third]
    return answer
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(maxSumOfThreeSubarrays(nums, k))