#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float('inf')] * (amount + 1)

        min_coins[0] = 0

        for coin in coins:
            for n in range(1, amount + 1):
                if coin <= n:
                    min_coins[n] = min(min_coins[n], min_coins[n - coin] + 1)

        return min_coins[amount] if min_coins[amount] != float('inf') else -1
