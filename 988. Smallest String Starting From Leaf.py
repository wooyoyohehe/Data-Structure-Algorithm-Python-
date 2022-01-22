# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        ans = ["{"]
        def helper(node, path, ans):
            if not node:
                return
            if not node.left and not node.right:
                ans[0] = min(ans[0], (path + chr(ord('a') + node.val))[::-1])
            helper(node.left, path + chr(ord('a') + node.val), ans)
            helper(node.right, path + chr(ord('a') + node.val), ans)
        helper(root, "", ans)
        return ans[0]

