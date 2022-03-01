# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        level = [root]
        while level:
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            leaves = level
            level = temp
        def helper(node):
            if not node:
                return None
            if node in leaves:
                return node
            left,right = helper(node.left), helper(node.right)
            if left and right:
                return node
            elif left:
                return left
            else:
                return right
        return helper(root)
        