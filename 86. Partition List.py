# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        small = ListNode(-1)
        small_begin = small
        large = ListNode(-1)
        large_begin = large
        while head:
            if head.val < x:
                small.next = ListNode(head.val)
                small = small.next
            else:
                large.next = ListNode(head.val)
                large = large.next
            head = head.next
        small.next = large_begin.next
        return small_begin.next