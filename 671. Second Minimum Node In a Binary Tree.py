# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = [float("inf"), float("inf")]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.val < a[0]:
                a[1],a[0] = a[0], node.val
            elif a[0] < node.val < a[1]:
                a[1] = node.val         
        dfs(root)
        if float("inf") == a[1]:
            return -1
        else:
            return a[1]
        
        