class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n == 1:
            if dungeon[0][0] >= 0:
                return 1
            else:
                return 1-dungeon[0][0]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if m == 1:
            if dungeon[0][n-1] >= 0:
                dp[0][n-1] = 0
            else:
                dp[0][n-1] = -dungeon[0][n-1]
            for i in range(n-2, -1, -1):
                if dungeon[0][i] <= 0:
                    dp[0][i] = dp[0][i+1] - dungeon[0][i]
                else:
                    if dp[0][i+1] - dungeon[0][i] >= 0:
                        dp[0][i] = dp[0][i+1] - dungeon[0][i]
                    else:
                        dp[0][i] = 0
        if n == 1:
            if dungeon[m-1][0] >= 0:
                dp[m-1][0] = 0
            else:
                dp[m-1][0] = -dungeon[m-1][0]
            for i in range(m-2, -1, -1):
                if dungeon[i][0] <= 0:
                    dp[i][0] = dp[i+1][0] - dungeon[i][0]
                else:
                    if dp[i+1][0] - dungeon[i][0] >= 0:
                        dp[i][0] = dp[i+1][0] - dungeon[i][0]
                    else:
                        dp[i][0] = 0
        
        if dungeon[m-1][n-1] >= 0:
            dp[m-1][n-1] = 0
        else:
            dp[m-1][n-1] = -dungeon[m-1][n-1]
            
        for i in range(n-2, -1, -1):
            if dungeon[m-1][i] <= 0:
                    dp[m-1][i] = dp[m-1][i+1] - dungeon[m-1][i]
            else:
                if dp[m-1][i+1] - dungeon[m-1][i] >= 0:
                    dp[m-1][i] = dp[m-1][i+1] - dungeon[m-1][i]
                else:
                    dp[m-1][i] = 0
        
        for i in range(m-2, -1, -1):
                if dungeon[i][n-1] <= 0:
                    dp[i][n-1] = dp[i+1][n-1] - dungeon[i][n-1]
                else:
                    if dp[i+1][n-1] - dungeon[i][n-1] >= 0:
                        dp[i][n-1] = dp[i+1][n-1] - dungeon[i][n-1]
                    else:
                        dp[i][n-1] = 0
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if dungeon[i][j] <= 0:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1])-dungeon[i][j]
                else:
                    if min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j] >= 0:
                        dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                    else:
                        dp[i][j] = 0 
        return dp[0][0]+1