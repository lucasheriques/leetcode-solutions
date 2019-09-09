#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


class Solution:
    def __init__(self):
        self.ans = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        self.subsetsHelper(sorted(nums), subset, 0)
        return self.ans

    def subsetsHelper(self, nums, subset, start):
        self.ans.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.subsetsHelper(nums, subset, i + 1)
            subset.pop()

    def powerset(array):
        subsets = [[]]
        for num in array:
            for i in range(len(subsets)):
                currentSubset = subsets[i]
                subsets.append(currentSubset + [num])
        return subsets
