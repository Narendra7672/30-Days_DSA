# Maximum Score of a Good Subarray:
def maximumScore(nums, k):
    left = right = k
    min_val = nums[k]
    max_score = min_val
    while left > 0 or right < len(nums) - 1:
        if left == 0:
            right += 1
        elif right == len(nums) - 1:
            left -= 1
        elif nums[left - 1] > nums[right + 1]:
            left -= 1
        else:
            right += 1
        min_val = min(min_val, nums[left], nums[right])
        max_score = max(max_score, min_val * (right - left + 1))
    return max_score
nums = [1, 4, 3, 7, 4, 5]
k = 3

print(maximumScore(nums, k))