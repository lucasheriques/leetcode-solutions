# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == total:
            return True

        total -= root.val

        return self.hasPathSum(root.left, total) or self.hasPathSum(root.right, total)
