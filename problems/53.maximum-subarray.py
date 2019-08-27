#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr = nums[0]

        for i in nums[1:]:
            curr = max(i, curr + i)
            max_sum = max(max_sum, curr)

        return max_sum
