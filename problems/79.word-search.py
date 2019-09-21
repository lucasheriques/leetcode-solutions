#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


class Solution:
    def exist(self, board, word) -> bool:
        rows = len(board)
        if rows == 0:
            return False
        cols = len(board[0])

        visited = [[False for j in range(cols)] for i in range(rows)]

        def search(i, j, word, word_pos):
            if word_pos >= len(word):
                return True
            char = word[word_pos]
            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or board[i][j] != char:
                return False
            visited[i][j] = True
            response = search(i + 1, j, word, word_pos + 1) or search(i - 1, j, word, word_pos + 1) \
                or search(i, j + 1, word, word_pos + 1) or search(i, j - 1, word, word_pos + 1)
            visited[i][j] = False
            return response

        for i in range(rows):
            for j in range(cols):
                if search(i, j, word, 0):
                    return True

        return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']]

Solution().exist(board, 'ABCCED')
