class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = [0 for _ in range(max(nums)+1)]
        for num in nums:
            arr[num] += 1
        ans = 0
        for i in range(len(arr)):
            if arr[i] > 0 and i+k<len(arr) and arr[i+k] > 0:
                ans += arr[i] * arr[i+k]
        return ans
        