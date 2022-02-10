# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_diff = abs(target-root.val)
        node = root
        ans = root.val
        while node:
            if target == node.val:
                return node.val
            elif target > node.val:
                if abs(target-node.val) < min_diff:
                    min_diff = abs(target-node.val)
                    ans = node.val
                node = node.right
            else:
                if abs(target-node.val) < min_diff:
                    min_diff = abs(target-node.val)
                    ans = node.val
                node = node.left
        return ans