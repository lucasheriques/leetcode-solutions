#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            current = stack.pop()

            if current is None:
                continue

            current.left, current.right = current.right, current.left
            stack.append(current.right)
            stack.append(current.left)

        return root
