# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans = 0
        def helper(node):
            if not node:
                return
            if node.val > high:
                helper(node.left)
            elif node.val < low:
                helper(node.right)
            else:
                self.ans += node.val
                helper(node.left)
                helper(node.right)
        helper(root)
        return self.ans