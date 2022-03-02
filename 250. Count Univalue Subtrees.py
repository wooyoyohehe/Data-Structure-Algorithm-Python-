# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.helper(root)
        return self.count
    
    def helper(self,node):
        if node is None:
            return True
        left = self.helper(node.left)
        right = self.helper(node.right)
        if (left and right and (node.left is None or node.val == node.left.val) and (node.right is None or node.val == node.right.val)):
            self.count += 1
            return True
        else:
            return False