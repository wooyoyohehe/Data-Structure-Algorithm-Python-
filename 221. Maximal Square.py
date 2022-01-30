class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i] == 1:
                ans = 1
        for j in range(m):
            dp[j][0] = int(matrix[j][0])
            if dp[j][0] == 1:
                ans = 1
        if m == 1 or n == 1:
            return ans
        for i in range(1, m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    ans = max(ans, dp[i][j])
        return ans*ans