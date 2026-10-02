# Count Even and Odd Numbers:

def count_EO(nums):
    even = 0
    odd = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even , odd
nums = [1,2,3,4,5,6,7]
res = count_EO(nums)
print(res)

nums = [1,2,3,4,5,6,7,8]
even = 0
odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:",even)
print("Odd:",odd)            
