# Find Peak Element:
def PeakElement(nums):
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n-1] > nums[n-2]:
        return n-1
    for i in range(1,n-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i
    return -1
nums = [1,2,3,4,2]
res=PeakElement(nums)
print(res)

def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
nums = [1, 2, 3, 4, 2]
print(findPeakElement(nums))