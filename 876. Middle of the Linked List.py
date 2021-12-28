# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None:
            return head
        node = ListNode(0)
        node.next = head
        length = 1
        while head.next:
            length += 1
            head = head.next
        index = length//2+1
        for i in range(index):
            node = node.next
        return node
        
        