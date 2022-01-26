# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        ans = []
        ans1 = []
        ans2 = []
        def dfs(node, ans):
            if not node:
                return
            dfs(node.left, ans)
            ans.append(node.val)
            dfs(node.right, ans)
        dfs(root1, ans1)
        dfs(root2, ans2)  
        p1 = p2 = 0
        while p1 < len(ans1) and p2 < len(ans2):
            if ans1[p1] <= ans2[p2]:
                ans.append(ans1[p1])
                p1 += 1
            else:
                ans.append(ans2[p2])
                p2 += 1
        if p1 == len(ans1):
            return ans + ans2[p2:]
        else:
            return ans + ans1[p1:]