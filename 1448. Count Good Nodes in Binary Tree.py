# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node, pre_max):
            if not node:
                return None
            if node.val >= pre_max:
                self.ans += 1
            pre_max = max(node.val, pre_max)
            dfs(node.left, pre_max)
            dfs(node.right, pre_max)
        dfs(root, root.val)
        return self.ans
        