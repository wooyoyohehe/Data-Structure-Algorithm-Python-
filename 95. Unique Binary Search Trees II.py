# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(left, right):
            all_trees = []
            if left > right:
                return [None]
            for i in range(left, right+1):
                left_trees = helper(left, i-1)
                right_trees = helper(i+1, right)
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        all_trees.append(node)
            return all_trees
        return helper(1, n)
                
                
                
        