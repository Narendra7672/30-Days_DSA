def moveZeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums        
nums = [1,2,0,40,23,0,1,2,3]  
s = moveZeroes(nums)  
print(s)        
