# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.ans = -float("inf")
        def helper(node):
            if not node:
                return [0,0]
            l_sum, l_count = helper(node.left)
            r_sum, r_count = helper(node.right)
            sub_sum = l_sum + r_sum + node.val
            count = l_count + r_count + 1
            self.ans = max(self.ans, (float(sub_sum)/count))
            return [sub_sum, count] 
        helper(root)
        return self.ans
            
        