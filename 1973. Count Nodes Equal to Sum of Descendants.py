# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0
        def helper(node):
            if not node:
                return 0
            sub_sum = helper(node.left) + helper(node.right)
            if sub_sum == node.val:
                self.ans += 1
            return sub_sum + node.val
        helper(root)
        return self.ans
        