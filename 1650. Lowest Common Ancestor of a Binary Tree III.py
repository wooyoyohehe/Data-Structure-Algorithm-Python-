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
        parent1 = [p]
        parent2 = [q]
        while p.parent or q.parent:
            if p.parent:
                if p.parent in parent2:
                    return p.parent
                else:
                    parent1.append(p.parent)
                    p = p.parent
            if q.parent:
                if q.parent in parent1:
                    return q.parent
                else:
                    parent2.append(q.parent)
                    q=q.parent
            