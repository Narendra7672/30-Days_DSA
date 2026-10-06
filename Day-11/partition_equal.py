# Partition Equal Subset Sum:
def partition_equal(nums):
    total = sum(nums)
    if total % 2 == 1:
      return False
    target = total // 2
    n = len(nums)
    def helper (idx,curr_sum):
       if curr_sum == target:
          return True
       if curr_sum > target or idx >= n:
          return False
       return helper(idx+1,curr_sum+nums[idx] or helper(idx + 1,curr_sum))
    return helper(0,0)
nums = [1,5,11,5]
res = partition_equal(nums)
print(res)

def partition_equal(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    n = len(nums)
    def helper(idx, curr_sum):
        if curr_sum == target:
            return True
        if curr_sum > target or idx >= n:
            return False
        return (helper(idx + 1, curr_sum + nums[idx]) or
                helper(idx + 1, curr_sum))
    return helper(0, 0)
nums = [1, 5, 11, 5]
res = partition_equal(nums)
print(res)