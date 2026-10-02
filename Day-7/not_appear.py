# Find the Number That Appears Only Once:
def not_appear(nums):
    result =0
    for num in nums:
        result = result ^ num
    return result
nums = [1,2,3,2,3]
res = not_appear(nums)
print(res)
# second way
def not_appear(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    for num in nums:
        if frequency[num] == 1:
            return num
nums = [1, 2, 3, 2, 3]
res = not_appear(nums)
print(res)