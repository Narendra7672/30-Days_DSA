# Product of Array Except Self:
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]  
    return res
nums = [1, 2, 3, 4]
print(f"Input:  {nums}")
print(f"Output: {productExceptSelf(nums)}")  # Expected output: [24, 12, 8, 6]
