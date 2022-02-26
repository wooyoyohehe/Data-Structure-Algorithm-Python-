"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.ans = 0
        def dfs(node, depth):
            if not node:
                return
            self.ans = max(self.ans, depth)
            for child in node.children:
                dfs(child, depth+1)
        dfs(root, 1)
        return self.ans