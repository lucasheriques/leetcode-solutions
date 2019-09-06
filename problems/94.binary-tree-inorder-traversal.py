#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []

        return self.inorderTraversalHelper(root, inorder)

    def inorderTraversalHelper(self, root: TreeNode, inorder) -> List[int]:
        if root is not None:
            self.inorderTraversalHelper(root.left, inorder)
            inorder.append(root.val)
            self.inorderTraversalHelper(root.right, inorder)

        return inorder

    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:
        stack, preorder = [root], []

        while stack:
            root = stack.pop()

            if root is not None:
                stack.append(root.right)
                stack.append(root.left)
                preorder.append(root.val)

        return preorder
