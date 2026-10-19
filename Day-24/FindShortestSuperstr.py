# Find the Shortest Superstring:
from collections import deque
def shortestSuperstring(words: list[str]) -> str:
    n = len(words)
    overlap = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j] = k
                        break
    queue = deque([(1 << i, i, words[i]) for i in range(n)])
    visited = {(1 << i, i): len(words[i]) for i in range(n)}
    shortest_superstring = None
    while queue:
        mask, last, curr_str = queue.popleft()       
        if visited.get((mask, last), float('inf')) < len(curr_str):
            continue          
        if mask == (1 << n) - 1:
            if shortest_superstring is None or len(curr_str) < len(shortest_superstring):
                shortest_superstring = curr_str
            continue        
        for nxt in range(n):
            if not (mask & (1 << nxt)):
                nxt_mask = mask | (1 << nxt)
                ol = overlap[last][nxt]
                nxt_str = curr_str + words[nxt][ol:]               
                if nxt_mask == (1 << n) - 1:
                    if shortest_superstring is None or len(nxt_str) < len(shortest_superstring):
                        shortest_superstring = nxt_str                
                if nxt_mask != (1 << n) - 1:
                    if nxt_mask not in visited or len(nxt_str) < visited[(nxt_mask, nxt)]:
                        visited[(nxt_mask, nxt)] = len(nxt_str)
                        queue.append((nxt_mask, nxt, nxt_str))                    
    return shortest_superstring
print(shortestSuperstring(["alex", "loves", "leetcode"]))
