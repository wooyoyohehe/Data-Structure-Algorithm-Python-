class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text2)
        m = len(text1)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] != text2[j]:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                else:
                    dp[i+1][j+1] = dp[i][j]+1
        return dp[-1][-1]