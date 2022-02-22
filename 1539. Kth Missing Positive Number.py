class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i,count = 1,0
        while count < k:
            if i not in arr:
                count += 1
            i += 1
        return i-1