class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        islands = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        dic = {}
        uf = UnionFind(m*n)
        index = 0
        ans = []
        for pos in positions:
            if (pos[0],pos[1]) in islands:
                ans.append(ans[-1])
                continue
            dic[(pos[0],pos[1])] = index
            index += 1
            parents = set()
            points = set()
            for dx,dy in directions:
                x = dx + pos[0]
                y = dy + pos[1]
                if 0<=x<m and 0<=y<n and (x,y) in islands:
                    points.add(dic[(x,y)])
                    parents.add(uf.find(dic[(x,y)]))
            for p in points:
                uf.union(index-1, p)
            if not ans:
                ans.append(1)
            else:
                ans.append(ans[-1]-len(parents)+1)
            islands.add((pos[0],pos[1]))
        return ans
                
                    
            
            