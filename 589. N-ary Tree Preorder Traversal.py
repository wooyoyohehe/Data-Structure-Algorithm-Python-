"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            for child in temp.children[::-1]:
                stack.append(child)
        return ans