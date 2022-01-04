# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = l1
        jinwei = 0
        while l1 and l2:
            if l1.val + l2.val + jinwei >= 10:
                l1.val = l1.val + l2.val - 10 + jinwei
                jinwei = 1
            else:
                l1.val = l1.val + l2.val + jinwei
                jinwei = 0
            if l1.next == None:
                l1_end_postion = l1
            l1 = l1.next
            l2 = l2.next

        if l1 == None and l2 == None:
            if jinwei == 1: 
                l1_end_postion.next = ListNode(1)
            return start
        
        if l1 == None:
            l1_end_postion.next = l2
            pointer = l2
        else:
            pointer = l1

        if pointer.val + jinwei != 10:
            pointer.val += jinwei
            return start
        else:
            while pointer.val == 9:
                pointer.val = 0
                if pointer.next == None:
                    pointer.next = ListNode(1)
                    return start
                pointer = pointer.next
            pointer.val += 1
            return start