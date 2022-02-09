# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        level = [root]
        while level:
            temp = []
            parent = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                    if node.left.val == x or node.left.val == y:
                        parent.append(node.val)
                if node.right:
                    temp.append(node.right)
                    if node.right.val == x or node.right.val == y:
                        parent.append(node.val)
            if len(parent) == 2:
                if parent[0] != parent[1]:
                    return True
                else:
                    return False
            level = temp
        return False