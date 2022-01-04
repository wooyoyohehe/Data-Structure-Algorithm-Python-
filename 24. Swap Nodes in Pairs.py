# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        cur = start
        if head == None or head.next == None: 
            return head
        while 1:
            if cur.next and cur.next.next:
                node1 = cur.next
                node2 = cur.next.next
                node3 = cur.next.next.next
                cur.next = node2
                node2.next = node1
                node1.next = node3
                cur = cur.next.next 
            if cur.next == None or cur.next.next == None:
                return start.next
        
        