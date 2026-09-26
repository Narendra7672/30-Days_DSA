'''Input:
nums = [2, 7, 11, 15]
target = 9

Output: [0, 1]



n = [2,6,11,3]
num = len(n)
target = 9
for i in range(num):
    for j in range(i+1,num):
        if n[i]+n[j] == target:
            print([i,j])  '''

def sum_two(nums,target):
    n = {}
    for i,num in enumerate(nums):
        complete = target - num
        if complete in n:
          return [n[complete],i]
        n[num]= i 
    return []   
            
nums = [2,6,11,3]
target = 9
n1 =sum_two(nums,target)
print(n1) 



          
      



