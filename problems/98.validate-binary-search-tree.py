#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, tree: TreeNode, min_value=float('-inf'), max_value=float('inf')) -> bool:
        if tree is None:
            return True

        if tree.val <= min_value or tree.val >= max_value:
            return False

        left_tree_valid = self.isValidBST(tree.left, min_value, tree.val)

        return left_tree_valid and self.isValidBST(tree.right, tree.val, max_value)
