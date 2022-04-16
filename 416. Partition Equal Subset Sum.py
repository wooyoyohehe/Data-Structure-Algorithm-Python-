class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % 2:
            return False
        col = sum(nums)//2
        row = len(nums)
        dp = [[False for _ in range(col+1)] for _ in range(row+1)]
        # initialize
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
        
            
        