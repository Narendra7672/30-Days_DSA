import heapq
from collections import Counter

def ReorganizeString(s):
    char_count = Counter(s)
    if max(char_count.values()) > (len(s) + 1) // 2:
        return ""
    max_heap = [
        (-count, char)
        for char, count in char_count.items()
    ]
    heapq.heapify(max_heap)
    res = []
    prev_count, prev_char = 0, ""
    while max_heap:
        count, char = heapq.heappop(max_heap)
        res.append(char)
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))
        prev_count, prev_char = count + 1, char
    return "".join(res)
print(ReorganizeString("aab"))    # aba
print(ReorganizeString("aaab"))   # ""
print(ReorganizeString("aaabbc")) # A valid rearrangement