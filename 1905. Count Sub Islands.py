class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m = len(grid2)
        n = len(grid2[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(pre_x, pre_y):
            if grid1[pre_x][pre_y] == 0:
                self.flag = False
            for d in directions:
                x = d[0]+pre_x
                y = d[1]+pre_y
                if 0<=x<m and 0<=y<n and grid2[x][y]==1:
                    grid2[x][y] = 2
                    dfs(x,y)
            return
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    self.flag = True
                    grid2[i][j] = 2
                    dfs(i,j)
                    if self.flag:
                        ans += 1
        return ans
            
                    
            
        