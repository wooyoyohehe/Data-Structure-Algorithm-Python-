class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        a = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            a[0][0] = 1
        else: 
            return 0
       
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                a[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                a[0][j] = 1
            else:
                break
        
        if m == 1 or n == 1:
            return a[m-1][n-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    a[i][j] = a[i-1][j]+a[i][j-1]
        return a[m-1][n-1]