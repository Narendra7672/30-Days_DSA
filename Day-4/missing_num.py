# Find the Missing Number:
def missing(num):
    n = len(num)
    n1 = n * (n+1) // 2
    n2 = sum(num)
    missing = n1 - n2
    return missing    
num = [0,1,3]
res = missing(num)
print(res)
# second 
def missing1(nums):
    n = len(nums)
    n1 = n * (n+1) // 2
    if n1 > 0:
      n2 = sum(nums)
      missing = n1-n2
    return missing
nums =  [0,1,3]
res = missing1(nums)
print(res)   
