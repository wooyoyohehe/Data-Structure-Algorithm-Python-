# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level = [root]
        ans = [root.val]
        while level:
            temp = []
            level_sum = 0
            for node in level:
                if node.left:
                    temp.append(node.left)
                    level_sum+=node.left.val
                if node.right:
                    temp.append(node.right)
                    level_sum+=node.right.val
            level = temp
            if len(level) != 0:
                ans.append(float(level_sum)/len(level))
        return ans