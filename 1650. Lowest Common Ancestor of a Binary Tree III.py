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
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        p1 = p
        q1 = q
        while p1 and q1:
            p1 = p1.parent
            q1 = q1.parent
        while p1:
            p = p.parent
            p1 = p1.parent
        while q1:
            q = q.parent
            q1 = q1.parent
        while p != q:
            p = p.parent
            q = q.parent
        return p
                
            
        