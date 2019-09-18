#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        if not rows:
            return []
        cols = len(matrix[0])

        is_col = False

        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        if is_col:
            for i in range(rows):
                matrix[i][0] = 0


Solution().setZeroes([[1, 1, 1], [0, 1, 2]])
