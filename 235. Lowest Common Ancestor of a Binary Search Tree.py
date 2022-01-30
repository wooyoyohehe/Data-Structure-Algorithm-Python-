# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        min_ = min(p.val, q.val)
        max_ = max(p.val, q.val)
        while 1:
            if min_ < root.val < max_ or root == p or root == q:
                return root
            elif root.val > max_:
                root = root.left
            elif root.val < min_:
                root = root.right