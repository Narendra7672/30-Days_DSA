import heapq
import sys
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

finder = MedianFinder()
for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    if parts[0] == "addNum" and len(parts) > 1:
        finder.addNum(int(parts[1]))
    elif parts[0] == "findMedian":
        print(finder.findMedian())
