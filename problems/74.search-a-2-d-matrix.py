#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1

        return False
