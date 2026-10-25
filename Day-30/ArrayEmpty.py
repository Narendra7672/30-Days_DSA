# Maximum Number of Operations to Make Array Empty:
from collections import Counter
import math

def minOperations(nums):
    count = Counter(nums)
    ops = 0
    for c in count.values():
        if c == 1:
            return -1
        ops += math.ceil(c / 3)
    return ops
nums =[1,3,2,4]
print(minOperations(nums))
