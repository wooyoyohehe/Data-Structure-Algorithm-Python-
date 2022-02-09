# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        temp = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            temp.append(node.val)
            inorder(node.right)
        inorder(root)
        left = 0
        right = len(temp) - 1
        while left<right:
            if temp[left]+temp[right]<k:
                left+=1
            elif temp[left]+temp[right]>k:
                right-=1
            else:
                return True
        return False