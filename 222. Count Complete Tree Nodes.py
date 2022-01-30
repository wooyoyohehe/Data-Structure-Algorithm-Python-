# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_h = 1
        right_h = 1
        root1 = root
        root2 = root
        while root1.left:
            left_h += 1
            root1 = root1.left
        while root2.right:
            right_h += 1
            root2 = root2.right
        if left_h == right_h:
            return 2 ** left_h - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)