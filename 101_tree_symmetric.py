# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # recursive
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L, R):
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return not root or isSym(root.left, root.right)
    # iterative
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        while queue:
            values = [i.val if i else None for i in queue]
            if values != values[::-1]:
                return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
    """
