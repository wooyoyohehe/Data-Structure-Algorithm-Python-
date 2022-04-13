class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        inf = 2**31-1
        visited = set()
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
        path = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                for dx, dy in directions:
                    new_x = x+dx
                    new_y = y+dy
                    if 0<=new_x<m and 0<=new_y<n and rooms[new_x][new_y]==inf and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        rooms[new_x][new_y] = path+1
                        q.append([new_x, new_y])
            path += 1
                
            
        