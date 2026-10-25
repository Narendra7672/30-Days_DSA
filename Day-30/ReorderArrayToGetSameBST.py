#Number of Ways to Reorder Array to Get Same BST:
import math


def numOfWays(nums):
    MOD = 10**9 + 7

    def ways(nums):
        if len(nums) <= 2:
            return 1
        root = nums[0]
        left = [x for x in nums[1:] if x < root]
        right = [x for x in nums[1:] if x > root]
        left_ways = ways(left)
        right_ways = ways(right)
        comb = math.comb(len(left) + len(right), len(left))
        return (comb * left_ways % MOD * right_ways % MOD) % MOD

    return (ways(nums) - 1) % MOD
nums = [2, 1, 3]
print(numOfWays(nums))
