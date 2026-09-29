# Remove Duplicates from a Sorted Array:
def remove_duplicates(nums):
    unique = []
    count = 0
    for num in nums:
        if num not in unique:
            unique.append(num)
            count += 1           
    return unique ,count    
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5]
res = remove_duplicates(nums)
print(res)         
# second approch
def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5]
count = remove_duplicates(nums)
print(count)
print(nums[:count])