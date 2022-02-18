# class Solution(object):
#     def shortestDistance(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         def bfs(i,j):
#             count = 0
#             path = 0
#             q = [[i,j,0]]
#             directions = [(-1,0), (0,-1),(0,1),(1,0)]
#             visited = [[False for _ in range(n)] for _ in range(m)]
#             visited[i][j] == True
#             while q:
#                 x,y,level = q.pop(0)
#                 for d in directions:
#                     new_x = x + d[0]
#                     new_y = y + d[1]
#                     if 0 <= new_x < m and 0 <= new_y < n:
#                         if grid[new_x][new_y] == 1:
#                             if not visited[new_x][new_y]:
#                                 visited[new_x][new_y] = True
#                                 count += 1
#                                 path += (level+1)
#                             if count == buildings or path >= ans:
#                                 return path
#                         elif grid[new_x][new_y] == 2:
#                             visited[new_x][new_y] = True
#                         else:
#                             if not visited[new_x][new_y]:
#                                 visited[new_x][new_y] = True
#                                 q.append([new_x, new_y,level+1])
#             return float("inf")
#         m = len(grid)
#         n = len(grid[0])
#         buildings = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     buildings += 1
                    
#         ans = float("inf")
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     ans = min(ans, bfs(i,j))
#         if ans == float("inf"):
#             return -1
#         return ans




class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(i,j):
            q = [[i,j,0]]
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[i][j] == True
            flag = False
            while q:
                x,y,level = q.pop(0)
                for d in directions:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if 0 <= new_x < m and 0 <= new_y < n:
                        if grid[new_x][new_y] == 0:
                            if not visited[new_x][new_y]:
                                visited[new_x][new_y] = True
                                table[new_x][new_y] += (level+1)
                                flag = True
                                q.append([new_x, new_y,level+1])
                        else:
                            visited[new_x][new_y] = True
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0 and visited[i][j] == False:
                        table[i][j] = float("inf")
            return flag
        directions = [(-1,0), (0,-1),(0,1),(1,0)]
        m = len(grid)
        n = len(grid[0])        
        table = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not bfs(i,j):
                        return -1
        ans = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = min(ans, table[i][j])
        if ans == float("inf"):
            return -1
        return ans
