# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        level = [root]
        while len(level) > 0:
            temp_level = []
            for node in level:
                temp_ans = node.val
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)
            ans.append(temp_ans)
            level = temp_level
        return ans