# Find the Second Largest Element
def second_large_num(num):
    first_large = num[0]
    for nums in num:
        if nums > first_large:
            first_large = nums
    second_large = num[0]
    for nums in num:
        if nums > second_large and nums != first_large:
            second_large = nums
    return second_large
num = [1,2,3,4,5,6,1,2,3,4]
res = second_large_num(num)
print(res)      
# second approch O(n)
num = [1,2,3,4,5,6,1,2,3,4]
first_nums = num[0]
sencond_nums = num[0]
for nums in num:
    if nums > first_nums:
        sencond_nums = first_nums
        first_nums = nums
    elif nums > sencond_nums and nums != first_nums:
        sencond_nums = nums
print(sencond_nums)
print(first_nums)             