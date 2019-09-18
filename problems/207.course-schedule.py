#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for x in range(numCourses)]

        # -1 -> vertex is being visited
        # 0 -> vertex was not visited
        # 1 -> vertex was already visited
        visited = [0 for x in range(numCourses)]

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
