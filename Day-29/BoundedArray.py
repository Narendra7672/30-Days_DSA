# Maximum Value at a Given Index in a Bounded Array:
def maxValue(n, index, maxSum):
    maxSum -= n
    def get_sum(length, value):
        if length == 0:
            return 0
        if value >= length:
            return length * (2 * value - length + 1) // 2
        return value * (value + 1) // 2
    left, right = 0, maxSum
    while left < right:
        mid = (left + right + 1) // 2
        left_sum = get_sum(index, mid - 1)
        right_sum = get_sum(n - index - 1, mid - 1)
        if mid + left_sum + right_sum <= maxSum:
            left = mid
        else:
            right = mid - 1
    return left + 1
n = 4
index = 1
maxSum = 4
print(maxValue(n, index, maxSum))
