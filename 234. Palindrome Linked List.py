# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head.next:
            return True
        if not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False
        slow = fast = head
        while 1:
            if fast.next == None:
                head1 = slow.next
                slow.next = None
                prev = ListNode(slow.val)
                prev.next = head1
                break
            elif fast.next.next == None:
                prev = slow.next
                slow.next = None
                break
            else:
                slow = slow.next
                fast = fast.next.next
        # reverse the 2nd part
        cur = prev
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True