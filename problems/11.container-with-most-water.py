#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


class Solution:
    def maxArea(self, height) -> int:
        # height is represented by the lowest value
        # length is represented by difference between the two indices
        left, right = 0, len(height) - 1

        max_area = 0

        while left < right:
            h = min(height[left], height[right])  # height
            l = right - left  # length

            max_area = max(max_area, h * l)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
