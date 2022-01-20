# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def backtrack(left, right):
            if left > right:
                return
            mid = (left+right) // 2
            node = TreeNode(nums[mid])
            node.left = backtrack(left, mid-1)
            node.right = backtrack(mid+1, right)
            return node
        root = backtrack(0, len(nums)-1)
        return root