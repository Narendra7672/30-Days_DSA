# Subarray Sum Equals K:
def subarraySum(nums: list[int], k: int) -> int:
    prefix_sums = {0: 1} 
    current_sum = 0
    count = 0  
    for num in nums:
        current_sum += num
        diff = current_sum - k
        if diff in prefix_sums:
            count += prefix_sums[diff]
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
    return count
if __name__ == "__main__":
    nums1 = [1, 1, 1]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {subarraySum(nums1, k1)}")  
    nums2 = [1, 2, 3]
    k2 = 3
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {subarraySum(nums2, k2)}")  # Output: 2 
