# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        def dfs(node):
            if not node:
                return None
            if node in nodes:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            elif left:
                return left
            else:
                return right
        return dfs(root)