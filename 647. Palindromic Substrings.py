class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[True for _ in range(len(s))] for _ in range(len(s))]
        ans = len(s)
        for j in range(len(s)):
            for i in range(j):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j]:
                    ans+=1
        return ans