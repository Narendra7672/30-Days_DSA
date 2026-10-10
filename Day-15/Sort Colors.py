# Sort Colors:
def SortColors(nums):
    zero,one,two = [],[],[]
    for num in nums:
        if num == 0:
            zero.append(num)
        elif num == 1:
            one.append(num)
        else:
            two.append(num)
    nums[:] = zero+one+two
    return nums
nums = [2, 0, 2, 1, 1, 0]
res = SortColors(nums)
print(res)

def SortColors(nums):
    low,mid,high = 0,0,len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
nums = [2, 0, 2, 1, 1, 0]
print(SortColors(nums))