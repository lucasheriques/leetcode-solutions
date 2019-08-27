# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # post-order is Left, Right, Root
    # this works by, if the value is a TreeNode, it means that is hasn't been visited yet.
    # when it's its value, the node has been visited so we can add it to our answer
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, TreeNode):
                    stack.append(temp.val)
                    stack.append(temp.right)
                    stack.append(temp.left)
                else:
                    res.append(temp)

        return res

    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return [] if not root else self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
    """
