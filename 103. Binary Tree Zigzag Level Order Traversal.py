# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        level = [root]
        flag = 1
        while len(level) > 0:
            temp_level = []
            temp_ans = []
            for node in level:
                if flag % 2 == 0:
                    temp_ans = [node.val] + temp_ans
                else:
                    temp_ans.append(node.val)
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right) 
            ans.append(temp_ans)
            level = temp_level
            flag += 1
        return ans
                