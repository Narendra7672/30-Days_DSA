# Count of Smaller Numbers After Self:
def countSmaller(nums: list[int]) -> list[int]:
    n = len(nums)
    counts = [0] * n
    indices = list(range(n))
    def merge_sort(left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid, right)
        temp = []
        i, j = left, mid
        right_smaller = 0
        while i < mid and j < right:
            if nums[indices[j]] < nums[indices[i]]:
                temp.append(indices[j])
                right_smaller += 1
                j += 1
            else:
                counts[indices[i]] += right_smaller
                temp.append(indices[i])
                i += 1
        while i < mid:
            counts[indices[i]] += right_smaller
            temp.append(indices[i])
            i += 1
        while j < right:
            temp.append(indices[j])
            j += 1
        indices[left:right] = temp
    merge_sort(0, n)
    return counts
print(countSmaller([5, 2, 6, 1]))  # [2, 1, 1, 0]
print(countSmaller([-1, -1]))      # [0, 0]
print(countSmaller([3, 2, 1]))     # [2, 1, 0]
print(countSmaller([]))            # []