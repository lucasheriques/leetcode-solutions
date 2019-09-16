#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        left, right = 0, len(s) - 1

        deleted = False

        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]

            left, right = left + 1, right - 1

        return True
