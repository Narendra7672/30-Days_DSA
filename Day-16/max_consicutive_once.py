# Longest Consecutive Ones After Flipping at Most One Zero:
def FindMaxConsecutiveOnce(nums):
    n = len(nums)
    max_count = 0
    for i in range(n):
        if nums[i] == 1:
            count = 0
            for j in range(i,n):
               if nums[j] == 1:
                  count += 1
               else:   
                  break
            max_count = max(count,max_count)
    return max_count
nums = [1,1,0,1,1,1]
res = FindMaxConsecutiveOnce(nums)
print(res)

def FindMaxConsecutiveOnce(nums):
    runs = []
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > 0:
                runs.append(count)
                count = 0
    if count > 0:
        runs.append(count)
    if len(runs) == 0:
        return 0
    return max(runs)  
nums = [1,1,0,1,1,1]
res = FindMaxConsecutiveOnce(nums)
print(res)                  