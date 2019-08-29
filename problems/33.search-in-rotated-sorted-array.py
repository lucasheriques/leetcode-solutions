#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        elif len(nums) == 1:
            return 0 if nums[0] == target else -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            # first half is sorted
            elif nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # second half is sorted
            elif nums[mid] <= nums[high]:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
