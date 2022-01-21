# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        ans = [True]
        def backtrack(node):
            if not node:
                return 0
            left_depth = backtrack(node.left)
            right_depth = backtrack(node.right)
            if abs(right_depth - left_depth) > 1:
                ans[0] = False
            return max(left_depth, right_depth) + 1
        backtrack(root)
        return ans[0]