# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level = [root]
        ans = []
        while level:
            temp = []
            for node in level:
                if node.left and (not node.right):
                    ans.append(node.left.val)
                    temp.append(node.left)
                if node.right and (not node.left):
                    ans.append(node.right.val)
                    temp.append(node.right)
                if node.left and node.right:
                    temp.append(node.left)
                    temp.append(node.right)
            level = temp
        return ans
                