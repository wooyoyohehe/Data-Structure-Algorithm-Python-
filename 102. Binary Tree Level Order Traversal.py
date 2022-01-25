# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        level = [root]
        while len(level)>0:
            temp_level = []
            temp_ans = []
            for node in level:
                temp_ans.append(node.val)
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)
            level = temp_level
            ans.append(temp_ans)
        return ans
            