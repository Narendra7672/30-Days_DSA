# Minimum Number of Platforms:
def find_minimum_platforms(arr, dep):
    arr.sort()
    dep.sort()
    n = len(arr)
    platforms_needed = 0
    max_platforms = 0
    i = 0
    j = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platforms_needed)
    return max_platforms

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(find_minimum_platforms(arr, dep))
