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

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        count = 0
        while count != k:
            smallest = float("inf")
            row = 0
            for i in range(len(matrix)):
                if len(matrix[i]) == 0:
                    continue
                if matrix[i][0] < smallest:
                    smallest = matrix[i][0]
                    row = i
            count += 1
            matrix[row].pop(0)
        return smallest