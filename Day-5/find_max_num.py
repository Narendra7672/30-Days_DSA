# Find the Largest Difference
'''
def find_max(nums):
    if not nums:
        return 0
    max_nums = 0
    min_nums = 0
    for num in nums:
        if num < min_nums:
            min_nums = num
        elif num - min_nums > max_nums:
            max_nums = num - min_nums
    return max_nums , min_nums

nums = [7, 1, 5, 3, 6, 4] 
res = find_max(nums)
print(res)      


nums = [7, 1, 5, 3, 6, 4]
min_num = nums[0]

for num in nums:
    if num < min_num:
        min_num = num
max_num = nums[0]       
for i  in range(1,len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]
print(max_num - min_num)  '''


def find_max(nums):
    min_num = nums[0]
    max_num = 0
    for num in nums:
        if num < min_num:
            min_num = num
        else: 
            difference = num -min_num
            if difference > max_num:
               max_num = difference 
    return max_num  
nums = [7, 1, 5, 3, 6, 4] 
res = find_max(nums)
print(res)                          
        
