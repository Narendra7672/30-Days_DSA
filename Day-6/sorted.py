# Check if Array is Sorted
'''
def sorted_array(nums):
    temp = 0
    sorted1 = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                if nums != nums:
                  return True
                else:
                  return False            

nums = [5,7,1,4,2,7,4,2,7,8,0]
res = sorted_array(nums)
print(res)'''

def array(num):
   for i in range(len(num)-1):
      if num[i] > num[i+1]:
        return False,num
      else:
         return True
      #return True, num
   #return num
num = [5,7,1,4,2,7,4,2,7,8,0]
res = array(num)
print(res) 

def array(num):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    return True
num = [5, 7, 1, 4, 2, 7, 4, 2, 7, 8, 0]
res = array(num)
print(res)
   