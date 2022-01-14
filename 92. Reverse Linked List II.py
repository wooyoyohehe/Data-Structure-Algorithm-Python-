# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        count = 1
        p = ListNode(-1)
        p.next = head
        if left == 1:
            before = p
            left_node = head
        for i in range(right):
            p = p.next
            if i == left - 2:
                before = p
                left_node = p.next
            if i == right - 1:
                right_node = p
                if p.next == None:
                    p.next = ListNode(501)
                after = p.next
        
        while count < right-left+1:
            p = ListNode(-1)
            p.next = head
            for _ in range(right-count):
                p = p.next
            end = p.next
            p.next = None
            end.next = p
            count += 1
        before.next = right_node
        if after.val != 501:
            left_node.next = after
        else:
            before.next = right_node
            left_node.next = None
        if left == 1:
            return before.next
        return head