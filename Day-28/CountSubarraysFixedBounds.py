# Count Subarrays With Fixed Bounds:
def countSubarrays(nums, minK, maxK):
    ans = 0
    min_i = -1
    max_i = -1
    bad_i = -1
    for i, num in enumerate(nums):
        if not (minK <= num <= maxK):
            bad_i = i
        if num == minK:
            min_i = i
        if num == maxK:
            max_i = i
        ans += max(0, min(min_i, max_i) - bad_i)
    return ans
nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
print(countSubarrays(nums, minK, maxK))
