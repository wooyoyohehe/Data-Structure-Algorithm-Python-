# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        q = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            heapq.heappush(q, (-abs(target-node.val),node.val))
            if len(q)>k:
                heapq.heappop(q)
            dfs(node.right)
        dfs(root)
        ans = []
        while q:
            ans.append(heapq.heappop(q)[1])
        return ans
        