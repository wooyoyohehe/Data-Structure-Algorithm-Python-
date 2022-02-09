class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        dp[start[0]][start[1]] = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = [[start,0]]
        while len(queue) > 0:
            pos, path = queue.pop(0)
            for dx,dy in directions:
                x,y = pos
                distance = 1
                x += dx
                y += dy
                while 0<=x<m and 0<=y<n and maze[x][y] != 1:
                    x += dx
                    y += dy
                    distance += 1
                if dp[x-dx][y-dy] > path+distance-1:
                    dp[x-dx][y-dy] = path+distance-1
                    queue.append([[x-dx,y-dy], path+distance-1])
        if dp[destination[0]][destination[1]] == float("inf"):
            return -1
        return dp[destination[0]][destination[1]]