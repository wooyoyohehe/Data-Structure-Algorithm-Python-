# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next
        if p2.next == None:
            while p1.next:
                p1 = p1.next
                headA = headA.next
        else:
            while p2.next:
                p2 = p2.next
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA