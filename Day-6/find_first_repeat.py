# Find the First Repeating Element:
def first_repeat(num):
    seen = set()
    for nums in num:
        if nums in seen:
            return nums
        seen.add(nums)
    return None
num = [1,2,3,4,21,4,3,5,3]
res = first_repeat(num)
print(res)
