# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def traverse(root):
            if root == None:
                return 
            traverse(root.left)
            traverse(root.right)
            if root:
                ans.append(root.val)
        traverse(root)
        return ans