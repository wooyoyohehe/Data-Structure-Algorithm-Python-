# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        end = head
        num = 0
        while end.next:
            num += 1
            end = end.next
        end.next = head
        
        for i in range(num-k%(num+1)):
            head = head.next
        start = head.next
        head.next = None
        return start