# Subarray With Given Sum:

def sumarray(nums,target):
    left = 0
    sum_array = 0
    for right in range(len(nums)):
        sum_array += nums[right]
        while sum_array > target:
            sum_array -= nums[left]
            left += 1
        if sum_array == target:
             return nums[left:right+1]   
nums = [1, 4, 20, 3, 10, 5]
target = 33
res = sumarray(nums,target)
print(res)        
            