# Find the Missing Ranges:
def missing_ranges(nums, lower, upper):
    result = []
    prev = lower - 1
    for num in nums:
        if num > prev + 1:
            start = prev + 1
            end = num - 1
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}---{end}")
        prev = num
    # Check the final range
    if prev < upper:
        start = prev + 1
        end = upper
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}---{end}")
    return result
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
res = missing_ranges(nums, lower, upper)
print(res)