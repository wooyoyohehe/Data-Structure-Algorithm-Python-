# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow = ListNode(-1)
        fast = ListNode(-1)
        slow.next = head
        fast.next = head

        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return None
            else:
                fast = fast.next.next 
                slow = slow.next
        slow = slow.next
        while head != slow:
            head = head.next
            slow = slow.next
        return slow