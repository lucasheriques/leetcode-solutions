#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

from bisect import bisect_left


class Solution:
    def threeSum(self, nums):
        sorted_nums = sorted(nums)

        ans = []

        for i in range(len(sorted_nums) - 2):
            a = sorted_nums[i]
            begin = i + 1
            end = len(sorted_nums) - 1
            while (begin < end):
                b, c = sorted_nums[begin], sorted_nums[end]
                if a + b + c == 0:
                    ans.append([a, b, c])
                    end, begin = end - 1, begin + 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    begin += 1

        return ans


q = Solution()
q.threeSum([-1, 0, 1, 2, -1, -4])
