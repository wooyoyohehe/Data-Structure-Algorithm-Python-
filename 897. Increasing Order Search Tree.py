# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        i = 1
        cur = TreeNode(nodes[0])
        new_root = cur
        while i < len(nodes):
            cur.right = TreeNode(nodes[i])
            i+=1
            cur = cur.right
        return new_root
            
            