# Maximum Sum Circular Subarray:
def maxSubarraySumCircular(nums):
    total = sum(nums)

    max_sum = nums[0]
    current_max = 0
    min_sum = nums[0]
    current_min = 0
    for num in nums:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)
    if max_sum < 0:
        return max_sum
    return max(max_sum, total - min_sum)
print(maxSubarraySumCircular([1, -2, 3, -2]))
print(maxSubarraySumCircular([5, -3, 5]))
print(maxSubarraySumCircular([-3, -2, -3]))