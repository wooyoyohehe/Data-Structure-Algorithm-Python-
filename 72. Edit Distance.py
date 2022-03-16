class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if not word1 or not word2:
            return max(m,n)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        flag = True
        for i in range(1, m):
            if word1[i] == word2[0] and flag and dp[0][0]!=0:
                dp[i][0] = dp[i-1][0]
                flag = False
            else:
                dp[i][0] = dp[i-1][0]+1
        flag = True
        for j in range(1,n):
            if word1[0] == word2[j] and flag and dp[0][0]!=0:
                dp[0][j] = dp[0][j-1]
                flag = False
            else:
                dp[0][j] = dp[0][j-1]+1
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
                
        