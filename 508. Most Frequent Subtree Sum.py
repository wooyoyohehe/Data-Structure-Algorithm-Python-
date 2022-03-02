# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic = dict()
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            temp_sum = node.val+left+right
            if temp_sum not in dic:
                dic[temp_sum] = 1
            else:
                dic[temp_sum] += 1
            return temp_sum
        helper(root)
        max_freq = 0
        for key in dic:
            if dic[key] > max_freq:
                max_freq = dic[key]
        ans = []
        for key in dic:
            if dic[key] == max_freq:
                ans.append(key)
        return ans
        