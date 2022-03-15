class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        self.parent[self.find(i)] = self.parent[j]

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(1001)
        for edge in edges:
            if uf.find(edge[0]) != uf.find(edge[1]):
                uf.union(edge[0], edge[1])
            else:
                return edge
        