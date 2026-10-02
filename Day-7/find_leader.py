# Find Leaders in an Array:
def leader(nums):
    max_right = nums[-1]
    leader = [nums[-1]]
    for i in range(len(nums) -2,-1,-1):
        if nums[i] > max_right:
            leader.append(nums[i])
            max_right = nums[i]
    return leader[::-1]
nums = [16, 17, 4, 3, 5, 2] 
res = leader(nums)
print(res)       
