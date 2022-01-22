# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        
        def helper(node, path, ans):
            if not node:
                return 
            path = path + "->" + str(node.val)
            if not node.left and not node.right:
                ans.append(path[2:])
                return
            helper(node.left, path, ans)
            helper(node.right, path, ans)
        helper(root, "", ans)
        return ans