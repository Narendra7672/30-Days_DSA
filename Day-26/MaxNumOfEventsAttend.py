# Maximum Number of Events That Can Be Attended:
import heapq
def maxEvents(events: list[list[int]]) -> int:
    events.sort()
    n = len(events)
    pos = 0
    time = 1
    attended = 0
    min_heap = []
    while pos < n or min_heap:
        if not min_heap:
            time = max(time, events[pos][0])
        while pos < n and events[pos][0] == time:
            heapq.heappush(min_heap, events[pos][1])
            pos += 1
        while min_heap and min_heap[0] < time:
            heapq.heappop(min_heap)
        if min_heap:
            heapq.heappop(min_heap)
            attended += 1
            time += 1
    return attended
events = [[1, 2], [2, 3], [3, 4], [1, 2]]
print(maxEvents(events))
