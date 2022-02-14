"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.pre = None
        self.head = None
        def helper(node):
            if not node:
                return None
            helper(node.left)
            if self.pre:
                self.pre.right = node
                node.left = self.pre
            else:
                self.head = node
            self.pre = node   
            helper(node.right)
        helper(root)
        self.pre.right = self.head
        self.head.left = self.pre
        return self.head