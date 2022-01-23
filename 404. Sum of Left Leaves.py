# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + helper(node.right)
            else:
                return helper(node.left) + helper(node.right)
        return helper(root)