# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return head
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        root = TreeNode(0)
        def helper(node, left, right, nums):
            mid = left+ (right-left)//2
            node.val = nums[mid]
            if left <= mid-1:
                node.left = TreeNode(0)
                helper(node.left, left, mid-1, nums)
            if mid+1<=right:
                node.right = TreeNode(0)
                helper(node.right, mid+1, right, nums)
        helper(root, 0, len(nums)-1, nums)
        return root