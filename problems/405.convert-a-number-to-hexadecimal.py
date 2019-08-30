#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#


class Solution:
    def toHex(self, num: int) -> str:
        digits = "0123456789abcdef"

        stack = []

        if num > 0:
            rem = num % 16
            stack.append(rem)
            num = num // 16
            print(rem, num)

        ans = ""
        while stack:
            ans += digits[stack.pop()]

        return ans


print(Solution().toHex(26))
