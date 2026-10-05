# Sliding Window Maximum:
def maxSliding(nums,k):
    if not nums:
        return []
    result = []
    queue = []
    for i in range(len(nums)):
        if queue and queue[0] < i - k+1:
            queue.pop(0)
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()

        queue.append(i)
        if i >= k-1:
            result.append(nums[queue[0]])
    return result
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = maxSliding(nums,k)
print(res)         