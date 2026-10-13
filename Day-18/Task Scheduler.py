# Task Scheduler:
from collections import Counter

def TaskScheduler(tasks, n):
    if n == 0:
        return len(tasks)
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = sum(1 for count in freq.values() if count == max_freq)
    intervals = (max_freq - 1) * (n + 1) + max_count
    return max(len(tasks), intervals)
tasks = ["A", "A", "A", "B", "B", "B"]
n = 3

print(TaskScheduler(tasks, n))