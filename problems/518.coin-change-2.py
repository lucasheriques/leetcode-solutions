#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1

        for coin in coins:
            for i in range(1, len(ways)):
                if i >= coin:
                    ways[i] += ways[i - coin]

        return ways[amount]
