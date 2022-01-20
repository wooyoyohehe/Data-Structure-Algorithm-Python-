# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = ans = ListNode(0)
        ans.next = head
        p.next = head
        while 1:
            if p.next == None:
                return ans.next
            elif p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
            