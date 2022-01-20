# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(node, temp, path, ans):
            if not node:
                return 
            if not node.left and not node.right:
                if temp + node.val == targetSum:
                    path += [node.val]
                    ans.append(path)
                return
            backtrack(node.left, temp+node.val, path + [node.val], ans)
            backtrack(node.right, temp+node.val, path + [node.val], ans)
        backtrack(root, 0, [], ans)
        return ans
            