# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # pre-order is Root, Left, Right
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return [] if not root else [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
    """
