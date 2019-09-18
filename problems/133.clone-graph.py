#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}

        def dfs(node):
            if not node:
                return
            else:
                node_copy = Node(node.val, [])
                dic[node] = node_copy
                for neighbor in node.neighbors:
                    if neighbor in dic:
                        node_copy.neighbors.append(dic[neighbor])
                    else:
                        node_copy.neighbors.append(dfs(neighbor))
                return node_copy
        return dfs(node)
