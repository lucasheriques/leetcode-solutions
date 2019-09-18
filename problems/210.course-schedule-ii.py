#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for x in range(numCourses)]

        # -1 -> vertex is being visited
        # 0 -> vertex was not visited
        # 1 -> vertex was already visited
        visited = [0 for x in range(numCourses)]

        order = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course, order):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for prereq in graph[course]:
                if not dfs(prereq, order):
                    return False
            visited[course] = 1
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course, order):
                return []
        return order
