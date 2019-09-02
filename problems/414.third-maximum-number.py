#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#


# O(n) time | O(n) space
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        output = [float("-inf")] * 3

        for n in nums:
            if n not in output:
                if n > output[2]:
                    output[0] = output[1]
                    output[1] = output[2]
                    output[2] = n
                elif n > output[1]:
                    output[0] = output[1]
                    output[1] = n
                elif n > output[0]:
                    output[0] = n

        if float("-inf") in output:
            return max(output)
        return output[0]
