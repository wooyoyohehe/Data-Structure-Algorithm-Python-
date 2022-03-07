class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        while arr[left] < arr[right]:
            left += 1
            right += 1
        return left