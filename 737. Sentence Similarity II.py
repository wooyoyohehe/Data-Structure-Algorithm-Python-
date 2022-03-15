class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)
        
class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False
        dsu = DSU(1001)
        idx = 0
        dic = {}
        for pair in similarPairs:
            if pair[0] not in dic:
                dic[pair[0]] = idx
                idx += 1
            if pair[1] not in dic:
                dic[pair[1]] = idx
                idx += 1
            dsu.union(dic[pair[0]], dic[pair[1]])
        for i in range(len(sentence1)):
            if sentence1[i] not in dic or sentence2[i] not in dic:
                if sentence1[i] != sentence2[i]:
                    return False
            elif dsu.find(dic[sentence1[i]]) != dsu.find(dic[sentence2[i]]):
                return False
        return True
            
        
        
        