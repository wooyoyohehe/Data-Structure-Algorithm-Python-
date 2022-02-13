# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def dfs(node, length):
            ans[0] = max(ans[0], length)
            if node.left:
                if node.left.val == node.val+1:
                    dfs(node.left, length+1)
                else:
                    dfs(node.left, 1)
            if node.right:
                if node.right.val == node.val+1:
                    dfs(node.right, length+1)
                else:
                    dfs(node.right, 1)
        dfs(root, 1)
        return ans[0]
            