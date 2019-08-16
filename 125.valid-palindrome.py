#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (31.97%)
# Likes:    656
# Dislikes: 1927
# Total Accepted:    390.1K
# Total Submissions: 1.2M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        s = s.lower()

        cleaned = "".join([c for c in s if c.isalnum()])

        return cleaned == cleaned[::-1]
