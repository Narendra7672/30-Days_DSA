# Longest Subarray With Sum K:
def subarray(nums,k):
    prefix_sum = 0
    max_length = 0
    first_index = {0: -1}
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum - k in first_index:
            length = i - first_index[prefix_sum - k]
            max_length = max(max_length, length)

        if prefix_sum not in first_index:
            first_index[prefix_sum] = i 
    return max_length      
nums = [10, 5, 2, 7, 1, 9]
k = 15
res = subarray(nums,k)
print(res)





          
