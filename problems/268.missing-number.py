#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)

        expectedNumbers = len(nums) + 1

        for num in range(expectedNumbers):
            if num not in nums:
                return num
