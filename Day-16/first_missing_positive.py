# First Missing Positive:

def FirstMissingPositive(nums):
    i = 1
    while True:
        if i not in nums:
            return i
        i += 1
nums = [1,2,0]
res = FirstMissingPositive(nums)
print(res)
# o(n)
def FirstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
    for i in range(n):
        if nums[i] != i+1:
            return i + 1
    return n + 1
nums = [1,2,0]
res = FirstMissingPositive(nums)
print(res)
            
        
