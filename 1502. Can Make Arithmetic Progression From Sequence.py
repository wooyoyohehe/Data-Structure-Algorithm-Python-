class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        start = min(arr)
        end = max(arr)
        interval = (end-start) // (len(arr)-1)
        if interval == 0:
            return start == end
        cur = start
        count = 0
        while cur in arr:
            cur += interval
            count += 1
        return count == len(arr)