# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = -float("inf"), upper = float("inf")):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        return helper(root)