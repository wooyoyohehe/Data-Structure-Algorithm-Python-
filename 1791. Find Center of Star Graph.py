class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = {}
        center = -1
        max_ = 0
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]] = 1
            else:
                dic[edge[0]] += 1
            if dic[edge[0]] > max_:
                max_ = dic[edge[0]]
                center = edge[0]
            if edge[1] not in dic:
                dic[edge[1]] = 1
            else:
                dic[edge[1]] += 1
            if dic[edge[1]] > max_:
                max_ = dic[edge[1]]
                center = edge[1]
        return center
        
        