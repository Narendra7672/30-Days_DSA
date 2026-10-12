# Find K Closest Elements:
def FindClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(FindClosestElements(arr, k, x))