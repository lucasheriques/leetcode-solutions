#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# O(n) time | O(1) space
class Solution:
    def fib(self, N: int) -> int:
        lastTwo = [0, 1]

        counter = 2

        while counter <= N:
            next = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = next
            counter += 1

        return lastTwo[1] if N > 0 else lastTwo[0]
