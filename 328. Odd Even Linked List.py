# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        even_head = ListNode(0)
        p = even_head
        left, mid, right = head, head.next, head.next.next
        while 1:
            left.next = right
            mid.next = None
            p.next = mid
            p = p.next
            if not right.next:
                right.next = even_head.next
                return head
            elif not right.next.next:
                p.next = right.next
                right.next = even_head.next
                return head
            else:
                left = left.next
                mid = left.next
                right = mid.next