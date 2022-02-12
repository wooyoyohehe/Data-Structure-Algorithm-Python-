class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans = sum(nums[:k])
        sum_ = sum(nums[:k])
        for i in range(1, len(nums)-k+1):
            sum_ = sum_-nums[i-1]+nums[i+k-1]
            ans = max(ans, sum_)
        return float(ans)/k