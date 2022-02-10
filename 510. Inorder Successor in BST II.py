"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right:
            node1 = node.right
            if not node1.left:
                return node1
            while node1.left:
                node1 = node1.left
            return node1
        else:
            node1 = node
            while node1.parent and node1.parent.val < node.val:
                node1 = node1.parent
            return node1.parent
        return None