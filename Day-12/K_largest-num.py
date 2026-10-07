# Kth Largest Element in an Array:

def findKthLargest(nums,k):
    import heapq
    heap = []
    for num in nums:
        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
nums = [3, 2, 1, 5, 6, 4]
k = 2
res = findKthLargest(nums,k)
print(res)  
nums = [1,2,3,4,5,5,5,67,6,5,5]
k = 1
res = findKthLargest(nums,k)
print(res)  
      
