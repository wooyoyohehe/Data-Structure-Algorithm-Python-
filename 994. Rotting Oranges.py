class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        queue = []
        count = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    count+=1
        new_rot = 0
        time = 0
        if count == 0:
            return 0
        while len(queue) > 0:
            temp_q = []
            for position in queue:
                for dx,dy in directions:
                    [x,y] = position
                    row = x+dx
                    col = y+dy
                    if not (0<=row<m and 0<=col<n):
                        continue
                    if grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    new_rot+=1
                    temp_q.append([row,col])
            time+=1
            queue = temp_q
        if new_rot != count:
            return -1
        return time-1