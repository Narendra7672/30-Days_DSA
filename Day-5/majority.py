# Find the Majority Element:

def majority(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    for num in nums:    
        if frequency[num] > len(nums) // 2:
            return num     
    return None
nums = [2, 2, 1, 1, 1, 2, 2, 1, 1] 
res = majority(nums)
print(res)      
