import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(q, matrix[i][j])
        for i in range(k-1):
            heapq.heappop(q)
        return heapq.heappop(q)