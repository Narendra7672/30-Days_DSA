def alienOrder(words):
    graph = {}
    indegree = {}
    for word in words:
        for ch in word:
            graph[ch] = []
            indegree[ch] = 0
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        for a, b in zip(w1, w2):
            if a != b:
                if b not in graph[a]:
                    graph[a].append(b)
                    indegree[b] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""
    queue = [ch for ch in indegree if indegree[ch] == 0]
    result = ""
    while queue:
        ch = queue.pop(0)
        result += ch
        for neighbor in graph[ch]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == len(indegree) else ""
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))