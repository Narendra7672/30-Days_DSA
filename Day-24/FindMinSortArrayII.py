# Find Minimum in Rotated Sorted Array II:
def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[right]:
            right = mid

        elif nums[mid] > nums[right]:
            left = mid + 1

        else:
            right -= 1
    return nums[left]
print(findMin([2, 2, 2, 0, 1]))  # 0
print(findMin([3, 3, 1, 3]))     # 1
print(findMin([1, 1, 1, 1]))     # 1
print(findMin([4, 5, 6, 1, 2, 3]))  # 1