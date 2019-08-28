#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -sys.maxsize - 1
        maxloc = minloc = 1

        for n in nums:
            prod1, prod2 = maxloc * n, minloc * n
            maxloc = max(n, max(prod1, prod2))
            minloc = min(n, min(prod1, prod2))
            ans = max(maxloc, ans)

        return ans
