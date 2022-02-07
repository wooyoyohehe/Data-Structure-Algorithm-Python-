# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = {}
        def helper(node, col, level):
            if not node:
                return
            if col not in dic:
                dic[col] = [[level, node.val]]
            else:
                dic[col].append([level, node.val])
            if node.left:
                helper(node.left, col-1, level+1)
            if node.right:
                helper(node.right, col+1, level+1)
        helper(root, 0, 0)
        ans = []
        for key in sorted(dic.keys()):
            dic[key].sort(key=lambda x:x[0])
            ans.append([])
            for i in dic[key]:
                ans[-1].append(i[1])
        return ans