#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for x in nums:
            if x - 1 not in nums_set:  # check if the number is the start of a streak
                y = x + 1
                while y in nums_set:
                    y += 1

                longest_streak = max(longest_streak, y - x)

        return longest_streak
