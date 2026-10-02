# Find the Second Smallest Element:

def find_small(nums):
    first_smallest = nums[0]
    second_smallest = nums[0]
    for num in nums:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num <  second_smallest and num != first_smallest:
            second_smallest = num  
    return second_smallest 
nums = [6,7,5,4,3,6,2,1,7,6]
res = find_small(nums)
print(res)        

