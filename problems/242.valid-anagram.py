#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
