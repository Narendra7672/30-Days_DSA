# Meeting Rooms II:
import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = []

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end)
    return len(heap)
print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(minMeetingRooms([[7, 10], [2, 4]]))