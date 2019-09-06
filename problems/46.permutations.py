#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


class Solution:
    def permute(self, array: List[int]) -> List[List[int]]:
        permutations = []
        self.permutationsHelper(0, array, permutations)
        return permutations

    def permutationsHelper(self, i, array, permutations):
        if i == len(array) - 1:
            permutations.append(array[:])
        else:
            for j in range(i, len(array)):
                self.swap(array, i, j)
                self.permutationsHelper(i + 1, array, permutations)
                self.swap(array, i, j)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
