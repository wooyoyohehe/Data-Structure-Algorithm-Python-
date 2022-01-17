# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        min_level = 10001
        def dfs(root, level, min_level):
            if not root.left and not root.right:
                min_level = min(level, min_level)
                return min_level
            if root.left:
                l1 = dfs(root.left, level+1,min_level)
            else:
                l1 = min_level
            if root.right:
                l2 = dfs(root.right, level+1,min_level)
            else:
                l2 = min_level
            return min(l1,l2)
        return dfs(root,1,min_level)