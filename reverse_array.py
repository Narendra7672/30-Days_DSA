def reverse_array(nums):
    temp = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    print()        
nums = [1, 2, 3, 4, 5]  
n = reverse_array(nums)
print(n) 


nums = [1,2,3,4,5]
temp = 0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
print()            
            
for i in range(0,len(nums)):
    print(nums[i],end="")


nums = [1,2,3,4,5]
left = 0
right = len(nums) - 1
while left < right:
    nums[left] , nums[right] = nums[right],nums[left]
    left += 1
    right -= 1
print(nums)    
