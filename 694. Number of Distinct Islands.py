class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        d = {(-1, 0),(1, 0),(0, -1),(0,1)}
        def dfs(pre_x, pre_y):
            for direction in d:
                x,y = pre_x+direction[0], pre_y+direction[1]
                if 0<=x<m and 0<=y<n and grid[x][y]==1:
                    grid[x][y] = 2
                    self.path.append((x-self.row, y-self.col))
                    dfs(x, y)
            return
        paths = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    self.row = i
                    self.col = j
                    self.path = []
                    dfs(i,j)
                    if self.path not in paths:
                        paths.append(self.path)
        return len(paths)
            

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        d = {"D":(-1, 0),"U":(1, 0),"L":(0, -1),"R":(0,1)}
        def dfs(pre_x, pre_y, direction):
            path = direction
            for key in d:
                x, y = pre_x+d[key][0], pre_y+d[key][1]
                if 0<=x<m and 0<=y<n and grid[x][y]==1:
                    grid[x][y] = 2
                    path += dfs(x, y, key)
            path += "0"
            return path
        paths = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    paths.add(dfs(i,j,"0"))
        return len(paths)