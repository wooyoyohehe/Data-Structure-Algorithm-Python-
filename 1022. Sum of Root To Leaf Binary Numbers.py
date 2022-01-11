# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        binary_num = ""
        def helper(root, binary_number, ans):
            binary_number += str(root.val)
            if not root.left and not root.right:
                ans.append(int(binary_number,2)) 
            if root.left:
                helper(root.left, binary_number, ans)
            if root.right:
                helper(root.right, binary_number, ans)
        helper(root, binary_num, ans)
        return sum(ans)