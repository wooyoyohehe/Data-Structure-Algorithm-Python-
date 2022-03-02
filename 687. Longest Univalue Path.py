# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
                5
               / \
              5   5 
    """
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.path = 0
        def helper(node):
            if not node:
                return 0
            l_path = helper(node.left)
            r_path = helper(node.right)
            cur_path = 0
            if node.left and node.val == node.left.val: 
                l_path += 1
                cur_path += l_path
            else:
                l_path = 0
            if node.right and node.val == node.right.val: 
                r_path += 1
                cur_path += r_path
            else:
                r_path = 0
            self.path = max(self.path, cur_path)
            return max(l_path, r_path)
        helper(root)
        return self.path
                
                