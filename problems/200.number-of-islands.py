#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for x in col] for col in grid]
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        return islands
