# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        successor = None
        flag = [False]
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)
        for i in range(len(nodes)):
            if nodes[i].val == p.val:
                if i == len(nodes)-1:
                    return None
                else:
                    return nodes[i+1]