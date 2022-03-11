# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right:
                return None
            temp_max = -1
            for i in range(left, right+1):
                if nums[i] > temp_max:
                    index = i
                    temp_max = nums[i]
            root = TreeNode(temp_max)
            root.left = helper(left, index-1)
            root.right = helper(index+1, right)
            return root
        return helper(0, len(nums)-1)
        