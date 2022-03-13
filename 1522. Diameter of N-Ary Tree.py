"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if not node.children:
                return 0
            max1 = 0
            max2 = 0
            for child in node.children:
                cur_depth = dfs(child) + 1
                if cur_depth > max1:
                    max2, max1 = max1, cur_depth
                elif cur_depth > max2:
                    max2 = cur_depth
            self.ans = max(self.ans, max1+max2)
            return max1
        dfs(root)
        return self.ans
        
        
        