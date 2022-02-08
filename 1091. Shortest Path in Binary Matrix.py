class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if grid == [[0]]:
            return 1
        n = len(grid)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = []
        queue.append([0, 0, 1])
        grid[0][0] = 1 
        while len(queue)>0:
            x, y, distance = queue.pop(0)
            for dx,dy in directions:
                row = dx+x
                col = dy+y
                if row==col==n-1:
                    return distance+1
                if not (0<=row<n and 0<=col<n) or grid[row][col] != 0:
                    continue
                grid[row][col] = 1
                queue.append([row,col, distance+1])
        return -1