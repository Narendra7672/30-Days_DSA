# Maximum Product Subarray:

def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]   
    for num in nums[1:]:
        current_sum = max(num, current_sum * num)
        max_sum = max(max_sum, current_sum)      
    return max_sum
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#nums = [2, 3, -2, 4] 
print(maxSubArray([2,3,-2,4]))
nums = [-2, 3, -4]
res = maxSubArray(nums)
print(res)

# Maximum Product Subarray:
def maxsubarray(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(n):
        product = 1
        for j in range(i,n):
            product *= nums[j]
            if product > max_sum:
                max_sum = product
    return max_sum
nums = [-2, 3, -4]
res = maxsubarray(nums)
print(res)
print(maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

def max_product(nums):
    current_max = nums[0]
    current_min = nums[0]
    max_product = nums[0]
    for num in nums[1:]:
        prev_max = current_max
        prev_min = current_min
        current_max = max(num, num * prev_max, num * prev_min)
        current_min = min(num, num * prev_max, num * prev_min)
        max_product = max(max_product, current_max)
    return max_product
print(max_product([2, 3, -2, 4]))
print(max_product([-2, 3, -4]))
        





