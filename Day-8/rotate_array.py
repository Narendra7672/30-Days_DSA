# Rotate Array by K Positions:
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return arr  
    k = k % n 
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1) 
    return arr
nums = [1, 2, 3, 4, 5, 6, 7]
print("Original Array: ", nums)
print("Rotated Right by 3:", rotate_right(nums.copy(), 3))
# Output: [5, 6, 7, 1, 2, 3, 4]
