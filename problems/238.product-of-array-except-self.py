#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


class Solution:
    def productExceptSelf(self, nums):
        output = list.copy(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    output[i] = output[i] * nums[j]

        return output


print(Solution().productExceptSelf([1, 2, 3, 4]))
