#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        begin, current, end = 0, 0, len(nums) - 1

        while current <= end:
            if nums[current] == 0:
                nums[begin], nums[current] = nums[current], nums[begin]
                begin, current = begin + 1, current + 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[end], nums[current] = nums[current], nums[end]
                end -= 1
