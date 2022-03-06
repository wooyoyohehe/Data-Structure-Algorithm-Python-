# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        dfs(root)
        left = 0
        right = len(nodes)-1
        def plant(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            nodes[mid].left = plant(left, mid-1)
            nodes[mid].right = plant(mid+1, right)
            return nodes[mid]
        return plant(left, right)
            

            
        