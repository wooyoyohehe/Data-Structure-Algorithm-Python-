# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = {}
        leaves = []
        def dfs(node):
            if not node:
                return None
            if node.left:
                dic[node.left] = node
            dfs(node.left)
            if node.right:
                dic[node.right] = node
            dfs(node.right)
            if not node.left and not node.right:
                leaves.append(node)
        dfs(root)
        ans = []
        visited = set()
        while leaves:
            temp = []
            leaf_vals = []
            for leaf in leaves:
                leaf_vals.append(leaf.val)
                visited.add(leaf)
                if leaf in dic:
                    parent = dic[leaf]
                    if (not parent.left or parent.left in visited) and (not parent.right or parent.right in visited):
                        temp.append(parent)
            leaves = temp
            ans.append(leaf_vals)
        return ans
                    