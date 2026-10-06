# Longest Increasing Subsequence:
def longest_subsequense(num):
    nums = (num)
    count = 0
    for i in range(len(nums)-2):
        increse = nums[i+1] + nums[i]
        if nums[i] > increse:
            count += 1
        else:
            increse = nums[i-1] + nums[i]
            if nums[i] > increse:
                count -= 1
    return count
num = [10,3,4,2,5,7,101,8]
res = longest_subsequense(num) 
print(res)

def long_subsequence(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i] , dp[j]+1) 
    return max(dp)
nums = [10, 9, 2, 5, 3, 7, 101, 18]
res = long_subsequence(nums)
print(res)            
    
            
