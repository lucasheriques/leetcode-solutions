#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


class Solution:
    def longestPalindrome(self, string: str) -> str:
        if len(string) == 0:
            return ""

        longest_palindrome = ""
        for i in range(len(string)):
            current_palindrome = string[i]
            # check for odd palindrome
            left, right = i - 1, i + 1
            while left >= 0 and right <= len(string) - 1 and string[left] == string[right]:
                current_palindrome = string[left:right+1]
                left, right = left - 1, right + 1

            longest_palindrome = current_palindrome if len(
                current_palindrome) > len(longest_palindrome) else longest_palindrome

            # checkfor even palindrome
            left, right = i, i + 1
            while left >= 0 and right <= len(string) - 1 and string[left] == string[right]:
                current_palindrome = string[left:right+1]
                left, right = left - 1, right + 1

            longest_palindrome = current_palindrome if len(
                current_palindrome) > len(longest_palindrome) else longest_palindrome

        return longest_palindrome
