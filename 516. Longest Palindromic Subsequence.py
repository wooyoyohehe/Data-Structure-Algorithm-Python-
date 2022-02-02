class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                    continue
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1]+2)
        return dp[0][-1]