# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node1, node2):
            if node2 == None and node1 == None:
                return True
            if (node1 == None or node2 == None) or node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root.left,root.right)