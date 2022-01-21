# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(-1)
        pre.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                node = cur.next
                cur.next = cur.next.next
                node.next = None
                p = pre
                while p.next.val <= node.val:
                    p = p.next
                next = p.next
                p.next = node
                node.next = next
            else:
                cur = cur.next
        return pre.next