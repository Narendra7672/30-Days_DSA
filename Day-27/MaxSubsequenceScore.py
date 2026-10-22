# Maximum Subsequence Score:
import heapq

def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
    min_heap = []
    current_sum = 0
    max_score = 0
    for a, b in pairs:
        heapq.heappush(min_heap, a)
        current_sum += a
        if len(min_heap) > k:
            current_sum -= heapq.heappop(min_heap)
        if len(min_heap) == k:
            max_score = max(max_score, current_sum * b)
    return max_score
print(maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3)) 
print(maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1))  # Output: 30