class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # day = 20
        # dp[20] = min[2, 7, 15] = 2
        # dp[8] = min[4, 9, 15] = 4
        # dp[7] = min[6, 9, 15] = 6
        # dp[6] = min[8, 9, 15] = 8
        # dp[4] = min[10, 9, 17] = 9
        # dp[1] = min[12, 11, 17] = 11
        dp = [0 for _ in range(days[-1]+1)]
        for i in range(1, days[-1]+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                one = costs[0]+dp[i-1] if i>=1 else costs[0]
                seven = costs[1]+dp[i-7] if i>=7 else costs[1]
                thirty = costs[2]+dp[i-30] if i>=30 else costs[2]
                dp[i] = min(one, seven, thirty)
        return dp[-1]