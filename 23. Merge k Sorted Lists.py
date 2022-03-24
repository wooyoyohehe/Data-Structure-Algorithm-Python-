# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        q = []
        for l in lists:
            if l:
                heapq.heappush(q, (l.val, l))
        while q:
            val, node = heapq.heappop(q)
            p.next = ListNode(node.val)
            p = p.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val, node))
        return head.next