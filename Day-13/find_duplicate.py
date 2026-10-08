# Find the Duplicate Number:
def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
nums1 = [1, 3, 4, 2, 2]
print(findDuplicate(nums1))  # 2
nums2 = [3, 1, 3, 4, 2]
print(findDuplicate(nums2))  # 3