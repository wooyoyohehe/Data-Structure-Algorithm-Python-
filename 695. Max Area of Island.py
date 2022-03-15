class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        def dfs(pos):
            area = 1
            for dx, dy in directions:
                x, y = pos[0]+dx, pos[1]+dy
                if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                    grid[x][y] = 2
                    area += dfs((x,y))
            return area
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    ans = max(ans, dfs((i,j)))
        return ans