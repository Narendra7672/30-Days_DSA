# Left Rotate an Array by One Position:
 
def left_rotate(nums):
    first = nums[0]
    for i in range(0, len(nums) -1):
        nums[i] = nums[i + 1]
    nums[-1] = first
    return nums
nums = [1,2,3,4]
res = left_rotate(nums)
print(res)
