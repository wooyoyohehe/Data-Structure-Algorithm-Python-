class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n = len(s2)
        m = len(s1)
        total_sum = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(len(s1)):
            total_sum += ord(s1[i])
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        for s in s2:
            total_sum += ord(s)   
        return total_sum - 2*dp[-1][-1]