#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        edits = [[x for x in range(len(word1) + 1)]
                 for y in range(len(word2) + 1)]
        for i in range(1, len(word2) + 1):
            edits[i][0] = edits[i - 1][0] + 1

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    edits[i][j] = edits[i - 1][j - 1]
                else:
                    edits[i][j] = 1 + min(edits[i - 1][j - 1],
                                          edits[i - 1][j], edits[i][j - 1])

        return edits[-1][-1]
