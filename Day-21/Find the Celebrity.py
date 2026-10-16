# Find the Celebrity:
def findCelebrity(knows):
    n = len(knows)
    candidate = 0
    for i in range(1, n):
        if knows[candidate][i] == 1:
            candidate = i
    for i in range(n):
        if i != candidate:
            if knows[candidate][i] == 1 or knows[i][candidate] == 0:
                return -1

    return candidate
knows = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]

print(findCelebrity(knows))