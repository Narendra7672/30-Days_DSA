# House Robber:

def rob(nums):
    n = len(nums)
    def helper(i):
        if  i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0],nums[1])
        return max(nums[i]+helper(i-2),helper(i-1))
    return helper(n-1)
nums = [1, 2, 3, 1]
res = rob(nums)
print(res)

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2 = 0
    prev1 = 0
    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current
    return prev1
nums = [1, 2, 3, 1]
print(rob(nums))