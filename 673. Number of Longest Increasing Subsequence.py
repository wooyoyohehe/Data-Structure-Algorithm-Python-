class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        count = [1] * len(nums)
        max_len = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
                        max_len = max(max_len, dp[i])
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        ans = 0
        for i in range(len(nums)):
            if dp[i] == max_len:
                ans += count[i]
        return ans