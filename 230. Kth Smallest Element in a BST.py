# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = []
        def helper(node, ans):
            if not node:
                return
            helper(node.left, ans)
            if len(ans) == k:
                return
            ans.append(node.val)
            helper(node.right, ans)
        helper(root,ans)
        return ans[-1]