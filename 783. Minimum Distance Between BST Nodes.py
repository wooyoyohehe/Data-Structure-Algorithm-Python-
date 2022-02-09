# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [float("inf")]
        temp = []
        def inorder(node):
            if not node:
                return 
            if node.left:
                inorder(node.left)
            if len(temp) == 0:
                temp.append(node.val)
            else:
                ans[0] = min(ans[0], abs(node.val-temp[0]))
                temp[0] = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return ans[0]