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
        self.count = 0
        def helper(node):
            if not node:
                return None
            left = helper(node.left)
            right = helper(node.right)
            if node == p or node == q:
                self.count += 1
                return node
            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        ans = helper(root)
        if self.count == 2:
            return ans
        else:
            return None
        
        