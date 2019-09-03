#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#


# O(n) time | O(n) space, where n is size of str
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if len(S) < 1:
            return ""

        total_shifts = 0

        chars = [char for char in S]

        for i in range(len(chars) - 1, -1, -1):
            total_shifts = (total_shifts + shifts[i] % 26) % 26
            chars[i] = chr((ord(chars[i]) - ord('a') +
                            total_shifts) % 26 + ord('a'))

        return "".join(chars)
