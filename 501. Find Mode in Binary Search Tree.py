# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic = dict()
        max_ = [0]
        def inorder(node):
            if not node:
                return 
            if node.left:
                inorder(node.left)
            if node.val not in dic:
                dic[node.val] = 1
            else:
                dic[node.val] += 1
            max_[0] = max(max_[0], dic[node.val])
            if node.right:
                inorder(node.right)
        inorder(root)
        ans = []
        for key in dic:
            if dic[key] == max_[0]:
                ans.append(key)
        return ans
        