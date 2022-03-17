"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        def my_insert(cur, node):
            next_ = cur.next
            cur.next = node
            node.next = next_
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        cur = head
        while cur.next.val >= cur.val:
            cur = cur.next
            if cur == head:
                break
        # cur is at the end of linked list
        if cur.next.val >= insertVal or cur.val <= insertVal:
            my_insert(cur, node)
            return head
        while cur.next.val < insertVal:
            cur = cur.next
        my_insert(cur, node)
        return head
        
        
		