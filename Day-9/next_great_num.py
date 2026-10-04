# Next Greater Element:
class Solution:
    def threeSumClosest(self,nums,target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2

def next_greater(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result
nums = [4, 5, 2, 10, 8]
res = next_greater(nums)
print(res)    #Output: [5, 10, 10, -1, -1]
