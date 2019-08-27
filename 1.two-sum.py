#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


class Solution:
    def twoSum(self, nums, target: int):
        table = {}
        for i, num in enumerate(nums):
            if target-num not in table:
                table[num] = i
            else:
                return [table[target-num], i]
