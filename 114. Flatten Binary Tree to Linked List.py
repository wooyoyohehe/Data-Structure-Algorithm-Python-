# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        node = root
        while 1:
            if node.left:
                temp_node = node.right
                node.right = node.left
                node.left = None
                while node.right:
                    node = node.right
                node.right = temp_node
                node = root
            elif not node.right:
                break
            else:
                node = node.right