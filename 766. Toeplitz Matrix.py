class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """        
        def judge(i,j):
            start = matrix[i][j]
            while i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != start:
                    return False
                else:
                    i += 1
                    j += 1
            return True
        for k in range(len(matrix)):
            if not judge(k,0):
                return False
        for l in range(len(matrix[0])):
            if not judge(0,l):
                return False
        return True