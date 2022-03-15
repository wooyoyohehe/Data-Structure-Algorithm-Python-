class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0),(1, 0),(0,-1),(0,1)]
        def dfs(pre_x, pre_y):
            for d in directions:
                x = d[0] + pre_x
                y = d[1] + pre_y
                if 0<=x<m and 0<=y<n and grid[x][y]==1:
                    grid[x][y] = 2
                    dfs(x,y)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        dfs(i,j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1
        return ans
        