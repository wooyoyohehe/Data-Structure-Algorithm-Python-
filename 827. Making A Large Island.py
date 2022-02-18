class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = dict()
        n = len(grid)
        directions = [(-1, 0),(1,0),(0,-1),(0,1)]
        code = 2
        def dfs(x,y,code):
            area = 1
            grid[i][j] = code
            for dx,dy in directions:
                if 0 <= x + dx < n and 0 <= y + dy < n:
                    if grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = code
                        area += dfs(x+dx, y+dy, code)
            return area
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dic[code] = dfs(i,j,code)
                    if dic[code] == n*n:
                        return n*n
                    code+=1
                    
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    temp,visited = 1, set()
                    for dx,dy in directions:
                        x,y = i+dx, j+dy
                        if 0<=x<n and 0<=y<n and grid[x][y] not in visited:
                            if grid[x][y] != 0:
                                temp += dic[grid[x][y]]
                                visited.add(grid[x][y])
                    ans = max(temp, ans)
        return ans