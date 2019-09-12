#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# O(n^2) time | O(n) space


class Solution:
    def threeSum(self, array, k=0):
        array.sort()
        ans = []

        for i in range(len(array) - 1):
            left = i + 1
            right = len(array) - 1
            if i > 0 and array[i] == array[i-1]:
                continue
            while left < right:
                potentialSum = array[i] + array[left] + array[right]
                if potentialSum == k:
                    ans.append([array[i], array[left], array[right]])
                    while left < right and array[left] == array[left+1]:
                        left += 1
                    while right > left and array[right] == array[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif potentialSum < k:
                    left += 1
                else:
                    right -= 1

        return ans
