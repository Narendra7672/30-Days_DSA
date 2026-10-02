# Rotate an Array by One Position: 
def rotate(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
    return nums
nums = [1,2,3,4]
res = rotate(nums)
print(res)  
# second 
def one(a):
    last = a[-1]
    for i in range(len(a),-1,0,-1):
        a[0] = last
    return a 
a = [1,2,3,4]
res = rotate(a)
print(res)   

def rotate(a):
    last = a[-1]
    for i in range(len(a) - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last
    return a
a = [4, 5, 6, 7]
res = rotate(a)
print(res)
