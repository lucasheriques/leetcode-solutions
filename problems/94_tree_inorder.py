# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # in-order is Left, Root, Right
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, node, inorder = [], root, []
        while node or stack:
            # keep going left
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        return inorder
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return [] if not root else self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
    """
