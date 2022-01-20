# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while 1:
            if fast.next == None or fast.next.next == None:
                cur = slow.next
                slow.next = None
                break
            else:
                fast = fast.next.next
                slow = slow.next
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head2 = prev
        start = ListNode(0)
        p = start
        start.next = head
        
        while head and head2:
            head_next = head.next
            head2_next = head2.next
            p.next = head
            p = p.next
            p.next = head2
            p = p.next
            head = head_next
            head2 = head2_next
        p.next = head
        return start.next