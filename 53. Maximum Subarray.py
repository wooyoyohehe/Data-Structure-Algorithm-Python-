class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp = [-10001]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]*(len(nums)+1)
        smallest = 0
        largest = -float("inf")
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
            largest = max(largest, prefix[i+1]-smallest)
            smallest = min(smallest, prefix[i+1])
        return largest

            