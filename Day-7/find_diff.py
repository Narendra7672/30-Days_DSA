# Find the Smallest Difference Between Two Elements:

def small_diff(num):
    num.sort()
    min_diff = float('inf')
    for i in range(len(num)-1):
        diff = num[i+1] - num[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff
num = [10, 3, 6, 20, 8]
res = small_diff(num)
print(res) 

nums = [10, 3, 6, 20, 8]
nums.sort()
min_diff = float('inf')
for i in range(len(nums) - 1):
    diff = nums[i + 1] - nums[i]
    if diff < min_diff:
        min_diff = diff
print(min_diff)      
