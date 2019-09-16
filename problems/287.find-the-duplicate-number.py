#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        assert len(nums) > 1

        slow = fast = finder = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        while True:
            slow = nums[slow]
            finder = nums[finder]

            if slow == finder:
                return slow
