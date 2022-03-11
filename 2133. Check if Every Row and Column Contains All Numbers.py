class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            s1 = set()
            s2 = set()
            for j in range(n):
                if 1 <= matrix[i][j] <= n:
                    s1.add(matrix[i][j])
                if 1 <= matrix[j][i] <= n:
                    s2.add(matrix[j][i])
            if len(s1) != n or len(s2) != n:
                return False
        return True
            
                        