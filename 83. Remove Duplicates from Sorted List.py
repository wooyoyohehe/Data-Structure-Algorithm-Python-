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
        start = ListNode(0)
        start.next = head
        left = head
        right = head.next
        while 1:
            if left.val == right.val:
                if right.next == None:
                    left.next = None
                    return start.next
                else:
                    right = right.next
            else:
                left.next = right
                left = right
                right = right.next
                if right == None:
                    return start.next