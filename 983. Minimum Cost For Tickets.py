class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(days[-1]+1)]
        j = 0
        for i in range(1, days[-1]+1):
            if i != days[j]:
                dp[i] = dp[i-1]
            else:
                j+=1
                one = costs[0]+dp[i-1] if i>=1 else costs[0]
                seven = costs[1]+dp[i-7] if i>=7 else costs[1]
                thirty = costs[2]+dp[i-30] if i>=30 else costs[2]
                dp[i] = min(one, seven, thirty)
        return dp[-1]