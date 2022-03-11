class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) % 2 == 1:
            bound = len(arr)
        else:
            bound = len(arr)-1
        ans = 0
        for length in range(1, bound+1, 2):
            for i in range(len(arr)-length+1):
                ans += sum(arr[i:i+length])
        return ans
            