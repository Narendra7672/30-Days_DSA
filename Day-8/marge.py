# Merge Overlapping Intervals:
def merge_intervals(intervals):
    if not intervals or len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    merged = []
    for current in intervals:
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            merged[-1][1] = max(merged[-1][1], current[1])
            
    return merged
example_input = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(example_input)
print("Merged Intervals:", result)
    # Output: [[1, 6], [8, 10], [15, 18]]
