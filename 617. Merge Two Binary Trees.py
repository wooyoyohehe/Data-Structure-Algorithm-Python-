# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def helper(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            if node1 and node2:
                node = TreeNode(node1.val+node2.val)
            node.left = helper(node1.left, node2.left)
            node.right = helper(node1.right, node2.right)
            return node
        return helper(root1, root2)