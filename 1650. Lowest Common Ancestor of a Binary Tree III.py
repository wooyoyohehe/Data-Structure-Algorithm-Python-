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
        p_depth,q_depth,p1,q1 = 0, 0, p, q
        while p1.parent:
            p_depth +=1
            p1 = p1.parent
        while q1.parent:
            q_depth +=1
            q1 = q1.parent
        if p_depth > q_depth:
            while p_depth > q_depth:
                p_depth -= 1
                p = p.parent
        else:
            while p_depth < q_depth:
                q_depth -= 1
                q = q.parent
        while p != q:
            p = p.parent
            q = q.parent
        return p