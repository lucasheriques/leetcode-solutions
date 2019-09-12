#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


class Solution:
    def fourSum(self, array, targetSum: int):
        pairSums = {}
        quadruplets = []

        for i in range(1, len(array) - 1):
            for j in range(i + 1, len(array)):
                currentSum = array[i] + array[j]
                difference = targetSum - currentSum
                if difference in pairSums:
                    for pair in pairSums[difference]:
                        quadruplets.append(pair + [array[i], array[j]])
            for k in range(0, i):
                currentSum = array[i] + array[k]
                if currentSum not in pairSums:
                    pairSums[currentSum] = [[array[i], array[k]]]
                else:
                    pairSums[currentSum].append([array[i], array[k]])

        return quadruplets


print(Solution().fourSum([7, 6, -4, -1, 1, 2], 16))
