class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        start = 0
        times = n-1
        number = 0
        while number < n*n:
            for j in range(times):
                number += 1
                matrix[start][start+j] = number
            for j in range(times):
                number += 1
                matrix[start+j][n-1-start] = number
            for j in range(times):
                number += 1
                matrix[n-1-start][n-1-start-j] = number
            for j in range(times):
                number += 1
                matrix[n-1-start-j][start] = number
            start += 1
            times -= 2
            if times == 0:
                number+= 1
                matrix[(n-1)//2][(n-1)//2] = number
        return matrix