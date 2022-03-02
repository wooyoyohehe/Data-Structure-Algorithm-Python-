# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def is_same(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return is_same(node1.left, node2.left) and is_same(node1.right, node2.right)
                    
        if not root:
            return False
        if is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot):
            return True
        else:
            return False
        
                            
        