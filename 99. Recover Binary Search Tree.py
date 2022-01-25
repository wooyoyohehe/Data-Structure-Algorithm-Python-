# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []
        def helper(node,nodes):
            if node == None:
                return
            helper(node.left, nodes)
            nodes.append(node)
            helper(node.right, nodes)
        helper(root, nodes)
        temp = []
        for i in range(len(nodes)-1):
            if nodes[i].val > nodes[i+1].val:
                temp.append(nodes[i])
                temp.append(nodes[i+1])
        if len(temp) == 2:
            temp[0].val, temp[1].val = temp[1].val, temp[0].val
        else:
            temp[0].val, temp[3].val = temp[3].val, temp[0].val