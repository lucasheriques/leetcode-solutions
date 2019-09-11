#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


class Solution:
    def numIslands(self, grid) -> int:
        islands = 0

        visited = [[False for value in row] for row in grid]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                islands = self.traverseNode(i, j, grid, visited, islands)

        return islands

    def traverseNode(self, i, j, matrix, visited, islands):
        nodesToVisit = [(i, j)]
        foundIsland = False

        while len(nodesToVisit) > 0:
            currentNode = nodesToVisit.pop()
            i, j = currentNode[0], currentNode[1]
            if visited[i][j]:
                continue
            visited[i][j] = True
            if matrix[i][j] == '0':
                continue
            foundIsland = True
            unvisitedNeighbors = self.getUnvisitedNeighbors(
                i, j, matrix, visited)
            for node in unvisitedNeighbors:
                nodesToVisit.append(node)

        if foundIsland:
            islands += 1

        return islands

    def getUnvisitedNeighbors(self, i, j, matrix, visited):
        unvisitedNeighbors = []
        if i > 0 and not visited[i - 1][j]:
            unvisitedNeighbors.append((i - 1, j))
        if i < len(matrix) - 1 and not visited[i + 1][j]:
            unvisitedNeighbors.append((i + 1, j))
        if j > 0 and not visited[i][j - 1]:
            unvisitedNeighbors.append((i, j - 1))
        if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
            unvisitedNeighbors.append((i, j + 1))
        return unvisitedNeighbors


matrix = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

print(Solution().numIslands(matrix))
