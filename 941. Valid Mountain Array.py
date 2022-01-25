class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left = 0
        right = len(arr)-1
        while left < len(arr)-1 and arr[left+1] > arr[left]:
            left += 1
        while right >= 1 and arr[right-1] > arr[right]:
            right -= 1
        if left == 0 or right == len(arr)-1:
            return False
        return left == right