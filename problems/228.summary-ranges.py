#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


class Solution:
    def summaryRanges(self, nums):
        response = []
        i = 0

        while i < len(nums):
            num = nums[i]
            next_num = None
            hasRange = False

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                hasRange = True
                next_num = nums[i + 1]
                i += 1

            response.append(self.formatRange(num, next_num))

            i += 1

        return response

    def formatRange(self, n1, n2):
        if n2:
            return f'{n1}->{n2}'
        return f'{n1}'


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
