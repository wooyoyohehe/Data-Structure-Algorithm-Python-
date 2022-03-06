# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node, cur_min, cur_max):
            if not node:
                return None
            self.ans = max(self.ans,abs(node.val-cur_min),abs(node.val-cur_max))
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            dfs(node.left, cur_min, cur_max)
            dfs(node.right, cur_min, cur_max)
        dfs(root, root.val, root.val)
        return self.ans
            