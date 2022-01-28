class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0]*len(triangle)
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i] = triangle[i][-1] + dp[i-1]
            for j in range(len(triangle[i])-2, 0 , -1):
                dp[j] = min(triangle[i][j] + dp[j], triangle[i][j] + dp[j-1])
            dp[0] = triangle[i][0] + dp[0]
        return min(dp)
