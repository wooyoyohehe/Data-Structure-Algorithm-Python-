# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        level = [root]
        ans = [root.val]
        while len(level)>0:
            temp = []
            temp_max = -float("inf")
            for node in level:
                if node.left:
                    temp.append(node.left)
                    temp_max = max(temp_max, node.left.val)
                if node.right:
                    temp.append(node.right)
                    temp_max = max(temp_max, node.right.val)
            level = temp
            if len(level) == 0:
                return ans
            ans.append(temp_max)
            