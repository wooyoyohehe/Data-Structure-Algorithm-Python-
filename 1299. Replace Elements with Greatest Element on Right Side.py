class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = [-1 for _ in range(len(arr))]
        for i in range(len(arr)-2, -1, -1):
            ans[i] = max(arr[i+1], ans[i+1])
        return ans
        