# Find the Largest Sum of Two Elements:

def largest_sum(nums):
    largest = []
    second_largest = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j]:
                largets = nums[i]+nums[j]          
    return largets 
nums = [1,2,3,4,5,6]
res = largest_sum(nums)
print(res) 
# second type           

def largest_sum(nums):
    largest = 0
    second_largest = 0
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return largest + second_largest
nums = [1, 2, 3, 4, 5, 6]
res = largest_sum(nums)
print(res)