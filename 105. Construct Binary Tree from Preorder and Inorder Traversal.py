# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # preorder = [3,9,20,15,7]
        # inorder = [9,3,15,20,7]
        def helper(preorder, inorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            root.left = helper(preorder[1:1+index], inorder[:index])
            root.right = helper(preorder[1+index:], inorder[index+1:])
            return root
        return helper(preorder, inorder)
            
            