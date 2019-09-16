#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits) - 1
        while i > 0:
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i - 1] += 1
            i -= 1
        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)
        return digits
