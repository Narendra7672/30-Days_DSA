def product_array(nums):
    n = len(nums)
    res = [1]*n
    left_product = 1
    for i in range(n):
        res[i] = left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(n-1,-1,-1):
        res[i] *= right_product
        right_product *= nums[i]
    return res
nums = [1,2,3,4,5]
n = product_array(nums)
print(n)        