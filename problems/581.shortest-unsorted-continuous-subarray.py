#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#


class Solution:
    def findUnsortedSubarray(self, array) -> int:
        smallest_oop = float('inf')
        largest_oop = float('-inf')
        smallest_index = float('inf')
        largest_index = 0

        for i in range(len(array)):
            num = array[i]
            if self.isOutOfOrder(i, num, array) and smallest_index > i:
                smallest_oop = array[i]
                smallest_index = i

        for i in range(len(array)):
            num = array[i]
            if self.isOutOfOrder(i, num, array) and largest_index < i:
                largest_index = i

        if smallest_index == float('-inf'):
            return 0

        lengthToSort = abs(smallest_index - largest_index) + 1
        return lengthToSort

    def isOutOfOrder(self, i, num, array):
        if i == 0:
            return num > array[i + 1]
        if i == len(array) - 1:
            return num < array[i - 1]
        return num > array[i + 1] or num < array[i - 1]


print(Solution().findUnsortedSubarray([1, 3, 2, 2, 2]))
