# Next Permutation:

def NextPermutation(nums):
    bp = -1
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            bp = i
            break
    if bp == -1: return nums.reverse()
    for i in range(len(nums)-1,bp,-1):
        if nums[bp]<nums[i]:
            nums[bp],nums[i] = nums[i],nums[bp]
            break
    nums[bp+1:] = reversed(nums[bp+1:])
    return nums
nums = [1, 2, 3]
res = NextPermutation(nums)
print(res)        