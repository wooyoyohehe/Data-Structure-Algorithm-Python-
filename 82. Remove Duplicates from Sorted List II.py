# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        start = ListNode(-1)
        start.next = head
        slow = start
        fast = start
        temp = 101
        while fast.next.next:
            if fast.next.val == fast.next.next.val:
                temp = fast.next.val
                while fast.next.val == temp:
                    fast = fast.next
                    if fast.next == None:
                        slow.next = None
                        return start.next
            else:
                fast = fast.next
                slow.next = fast
                slow = slow.next
        slow.next = fast.next
        
        return start.next