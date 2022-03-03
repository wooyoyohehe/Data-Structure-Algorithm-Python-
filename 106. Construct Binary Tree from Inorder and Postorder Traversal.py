# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # inorder = [9,3,15,20,7] //left, root, right
        # postorder = [9,15,7,20,3] //left, right, root
        def helper(inorder, postorder):
            if not inorder:
                return None
            root = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            root.left = helper(inorder[:index], postorder[:index])
            root.right = helper(inorder[index+1:], postorder[index:-1])
            return root
        return helper(inorder, postorder)
            
        