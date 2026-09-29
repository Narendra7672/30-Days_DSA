# Find the First Non-Repeating Element

def non_repeating(nums):
    n = []
    for num in nums:
        if num not in n:
            n.append(nums)
    return n
nums = [1,1,2,3,2,4,5,4,6,7,7]
res = non_repeating(nums)
print(res)    


def first_non_repeating(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    for num in nums:
        if frequency[num] == 1:
            return num
    return None

nums = [4, 5, 1, 2, 1, 4,9,7, 5]

result = first_non_repeating(nums)

print(result)
