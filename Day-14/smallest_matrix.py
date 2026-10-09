# Kth Smallest Element in a Sorted Matrix:

import heapq
def kthSmallest(matrix, k):
    heap = []
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    for _ in range(k - 1):
        heapq.heappop(heap)
    return heapq.heappop(heap)
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8

print(kthSmallest(matrix, k))