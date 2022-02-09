class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m = len(maze)
        n = len(maze[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = [start]
        while len(queue) > 0:
            x,y = queue.pop(0)
            if [x,y] == destination:
                return True
            for dx,dy in directions:
                row = x+dx
                col = y+dy
                if not (0<=row<m and 0<=col<n):
                    continue
                if maze[x][y] == 1:
                    continue
                # conditions of while should be noticed, whether it is 1 or 2 or 0 is important
                # 1 is wall, 2 is visited, 0 is empty
                # DONT use 1 for visited, or you build the walls that are not exist
                while 0<=row<m and 0<=col<n and maze[row][col] != 1:
                    row += dx
                    col += dy
                if maze[row-dx][col-dy] == 2:
                    continue
                queue.append([row-dx,col-dy])
                maze[row-dx][col-dy] = 2
        return False

