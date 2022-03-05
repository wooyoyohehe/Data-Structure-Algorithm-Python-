# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        def dfs(node, parent):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        visited = set()
        visited.add(target)
        q = [target]
        length = 0
        while length < k and q:
            for i in range(len(q)):
                cur = q.pop(0)
                for node in cur.left, cur.right, cur.parent:
                    if node and node not in visited:
                        q.append(node)
                        visited.add(node)
            length += 1
        ans = []
        for node in q:
            ans.append(node.val)
        return ans