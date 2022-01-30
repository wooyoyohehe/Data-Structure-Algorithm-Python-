"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        level = [root]
        while len(level) != 0:
            temp_level = []
            for i in range(len(level)):
                if i != len(level)-1:
                    level[i].next = level[i+1]
                if level[i].left:
                    temp_level.append(level[i].left)
                if level[i].right:
                    temp_level.append(level[i].right)
            level[-1].next = None
            level = temp_level
        return root