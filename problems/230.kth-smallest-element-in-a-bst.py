#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Assuming the tree is balanced:
# We first found the lowest value that is a leaf
# Then we go back up, until we find the kth smallest value
# Time complexity is O(H + k), where H is the height of the tree, since
#  we must iterate until we find a leaf, than k times til we find kth.
#  If the tree is balanced, H = logN, where N is number of nodes.
# Space complexity is O(H + k), O(N + k) in worst case, O(logN + k) in the avg.
#  Avg happens when the tree is balanced. Worst if the tree is like a linked list
#  (all nodes in one side).
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()

            k -= 1
            if k == 0:
                return root.val

            root = root.right

        return -1
