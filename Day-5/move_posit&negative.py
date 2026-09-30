# Move All Negative Numbers to One Side:

def one_side(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] < 0:
            left += 1
        elif nums[right] >= 0:
           right -= 1    
        else:    
          nums[left],nums[right] = nums[right],nums[left]   
    return nums
nums = [1,-12,3,4,-1,-2,-3,-4]
res = one_side(nums)
print(res)        

'''
nums = [1,-12,3,4,-1,-2,-3,-4]
for i in range(len(nums)):
  if nums[i] >= 0:
     print("positive",nums[i])

  else:
     print("negative",nums[i])'''
