class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        ans = 1
        
        def dfs(i,j):
            if dp[i][j] == 0:
                if i > 0 and matrix[i][j] < matrix[i-1][j]:
                    left = dfs(i-1, j)
                else:
                    left = 0
                if i < m-1 and matrix[i][j] < matrix[i+1][j]:
                    right = dfs(i+1, j)
                else:
                    right = 0
                if j > 0 and matrix[i][j] < matrix[i][j-1]:
                    down = dfs(i,j-1)
                else:
                    down = 0
                if j < n-1 and matrix[i][j] < matrix[i][j+1]:
                    up = dfs(i,j+1)
                else:
                    up = 0
                dp[i][j] = 1+max(left, right, down, up)
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
        return ans
                    