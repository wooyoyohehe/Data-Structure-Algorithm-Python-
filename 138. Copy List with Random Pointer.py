"""
Solution 1
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        copied_head = Node(0)
        p = head
        q = copied_head
        dic = {}
        while p:
            temp = Node(p.val) 
            q.next = temp
            q = q.next
            dic[p] = q
            p = p.next
        p = head
        q = copied_head.next
        while p:
            if not p.random:
                q.random == None
            else:
                q.random = dic[p.random]
            p = p.next
            q = q.next
        return copied_head.next




"""
Solution 2 O(N)
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        p = head
        while p:
            next_node = p.next
            p.next = Node(p.val)
            p.next.next = next_node
            p = p.next.next
        p = head
        while p:
            random_node = p.random
            if not random_node:
                p.next.random = None
            else:
                p.next.random = random_node.next
            p = p.next.next
        p = head
        copied_head = p.next
        while p.next.next:
            next_node = p.next.next
            p.next.next = p.next.next.next
            p.next = next_node
            p = p.next
        p.next = None
        return copied_head