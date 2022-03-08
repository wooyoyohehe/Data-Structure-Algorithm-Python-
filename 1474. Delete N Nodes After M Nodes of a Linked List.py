# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        ans = head
        p = ListNode(0)
        p.next = head
        q = p
        while 1:
            for i in range(m):
                if p.next:
                    p = p.next
                else:
                    return head
            q = p
            for j in range(n+1):
                if q:
                    q = q.next
                else:
                    p.next = None
                    return head
            p.next = q
            q = p
            