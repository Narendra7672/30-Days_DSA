# Find the Minimum Number of Days to Make m Bouquets:

def minDays(bloomDay,m,k):
    if len(bloomDay) < m * k:
        return -1
    def getBouquetCount(waitingDays):
        bouquet_count = 0
        required_flowers = k
        for day in bloomDay:
            if day > waitingDays:
                required_flowers = k
            else:
                required_flowers -= 1
                if required_flowers == 0:
                    bouquet_count += 1
                    required_flowers = k
        return bouquet_count
    l, r = min(bloomDay), max(bloomDay)
    while l < r:
        mid = (l + r) // 2
        if getBouquetCount(mid) >= m:
            r = mid
        else:
            l = mid + 1
    return l
bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
print(minDays(bloomDay, m, k))
