# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, path):
            if not node:
                return 0
            if not node.left and not node.right:
                return int(path+str(node.val))
            return helper(node.left, path + str(node.val)) + helper(node.right, path + str(node.val))
        return helper(root, "")