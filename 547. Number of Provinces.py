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
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(200)
        dic = {}
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j]:
                    uf.union(i,j)
        ans = set()
        for i in range(len(isConnected)):
            ans.add(uf.find(i))
        return len(ans)