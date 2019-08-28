#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # obvious O(n2) solution is min(nums)
        # but we can do better with a Binary Search variant
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            # check if there's rotation
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
