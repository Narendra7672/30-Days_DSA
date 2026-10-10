# Find First and Last Position of an Element in a Sorted Array:
def FindFirstLastElement(nums,target):
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first,last]
nums = [1,2,3,4,5,4,5,6,7]
target = 5
res = FindFirstLastElement(nums,target)
print(res)    

def searchRange(nums, target):
    def findPosition(find_first):
        left,right,position = 0,len(nums),-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                position = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return position
    first = findPosition(True)
    last = findPosition(False)
    return [first, last]
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(searchRange(nums, target))
