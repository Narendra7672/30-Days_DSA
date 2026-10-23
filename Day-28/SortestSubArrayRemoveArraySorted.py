# Shortest Subarray to Be Removed to Make Array Sorted:
def findLengthOfShortestSubarray(arr):
    n = len(arr)
    left = 0
    while left + 1 < n and arr[left] <= arr[left + 1]:
        left += 1
    if left == n - 1:
        return 0
    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1
    ans = min(n - left - 1, right)
    i, j = 0, right
    while i <= left and j < n:
        if arr[i] <= arr[j]:
            ans = min(ans, j - i - 1)
            i += 1
        else:
            j += 1
    return ans
print(findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
