# Remove All Occurrences of a Given Element

def remove_occur_nums(nums,target):
    result = []
    for num in nums:
        if num != target:
            result.append(num)
    return result
nums = [3,2,2,3]
target = 3
res = remove_occur_nums(nums,target) 
print(res)       

def remove_occur_nums(nums,target):
    result = 0
    for num in nums:
        if num != target:
            nums[result]=num
            result += 1
    return result
nums = [3,2,2,3]
target = 3
res = remove_occur_nums(nums,target) 
print(res)       
